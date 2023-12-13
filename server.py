import logging
from concurrent import futures
from datetime import datetime
import time

import grpc
import a3_pb2
import a3_pb2_grpc

# Dummy storage to simulate in-memory storage
class DummyStorage:
    def __init__(self):
        self.posts = {}
        self.comments = {}
        self.subreddits = {}

    # Implement methods to handle storage of posts, comments, subreddits, etc.
    def create_post(self, post):
        self.posts[post.post_id] = post
    
    def get_post_by_id(self, post_id):
        return self.posts.get(post_id)
    
    def create_comment(self, comment):
        parent_comment = self.comments.get(comment.parent_comment_id)
        if (parent_comment):
            parent_comment.has_replies = True
            parent_comment.sub_comments.append(comment)
        self.comments[comment.comment_id] = comment
    
    def get_comment_by_id(self, comment_id):
        return self.comments.get(comment_id)

    def get_comments_by_post_id(self, post_id):
        filtered_comments = [comment for comment in self.comments.values() if comment.post_id == post_id]
        return filtered_comments
    
    def get_comments_by_comment_id(self, comment_id):
        comment = self.comments.get(comment_id)
        return comment.sub_comments
    
    def get_post_score(self, post_id):
        return self.posts.get(post_id).score if post_id in self.posts else None

    def get_comment_score(self, comment_id):
        return self.comments.get(comment_id).score if comment_id in self.comments else None


class RedditServicer(a3_pb2_grpc.RedditServiceServicer):
    def __init__(self):
        self.storage = DummyStorage()

    def CreatePost(self, request, context):
        post = a3_pb2.Post(
            post_id = str(len(self.storage.posts) + 1),
            title = request.title,
            text=request.text,
            author_id=request.author_id,
            score=0,
            state=a3_pb2.Post.NORMAL,
            #publication_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Current timestamp
            subreddit_id=request.subreddit_id
        )
        self.storage.create_post(post)
        return post

    def VotePost(self, request, context):
        post_id = request.entity_id
        post = self.storage.get_post_by_id(post_id)

        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post not found")
            return a3_pb2.Post()
        
        if request.is_upvote:
            post.score += 1
        else:
            post.score -= 1
        
        self.storage.posts[post_id] = post
        return post

    def GetPostContent(self, request, context):
        post_id = request.post_id
        post = self.storage.get_post_by_id(post_id)
        if post:
            return post
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post not found")
            return a3_pb2.Post()
    
    def CreateComment(self, request, context):
        comment = a3_pb2.Comment(
            comment_id = str(len(self.storage.comments) + 1),
            post_id = request.post_id,
            parent_comment_id = request.parent_comment_id,
            author_id = request.author_id,
            text = request.text,
            score = 0,
            state = a3_pb2.Comment.NORMAL,
            #publication_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            has_replies= False
        )
        self.storage.create_comment(comment)
        return comment
    
    def VoteComment(self, request, context):
        comment_id = request.entity_id
        comment = self.storage.get_comment_by_id(comment_id)

        if not comment:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Comment not found")
            return a3_pb2.Comment()
        
        if request.is_upvote:
            comment.score +=1
        else:
            comment.score -=1
        
        self.storage.comments[comment_id] = comment
        return comment
    
    def GetMostUpvotedComments(self, request, context):
        post_id = request.post_id
        comments = self.storage.get_comments_by_post_id(post_id)
        sorted_comments = sorted(comments, key=lambda x: x.score, reverse=True)
        n = request.limit
        most_upvoted = sorted_comments[:n]
        return a3_pb2.CommentsResponse(comments=most_upvoted)
    
    def ExpandCommentBranch(self, request, context):
        comment_id = request.comment_id
        sub_comments = self.storage.get_comments_by_comment_id(comment_id)

        comment_tree = a3_pb2.CommentTree()
        
        sorted_sub_comments = sorted(sub_comments, key=lambda x: x.score, reverse=True)

        n = request.limit
        most_upvoted_sub_comments = sorted_sub_comments[:n]
        comment_tree.comments.extend(most_upvoted_sub_comments)

        for comment in most_upvoted_sub_comments:
            sub_comments_response = a3_pb2.CommentsResponse(comments=comment.sub_comments[:n])
            comment_tree.replies[comment.comment_id].CopyFrom(sub_comments_response)
        return comment_tree

    def MonitorUpdates(self, request, context):
        post_id = request.post_id
        while True:
            post_score = self.storage.get_post_score(post_id)
            if post_score is not None:
                yield a3_pb2.ScoreUpdates(entity_id=post_id, new_score=post_score)

            comments = self.storage.get_comments_by_post_id(post_id)
            for comment in comments:
                comment_score = self.storage.get_comment_score(comment.comment_id)
                if comment_score is not None:
                    yield a3_pb2.ScoreUpdates(entity_id=comment.comment_id, new_score=comment_score)
            time.sleep(5) 


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    a3_pb2_grpc.add_RedditServiceServicer_to_server(RedditServicer(), server)
    port = 4000  # Define port as an integer
    server.add_insecure_port("[::]:" + str(port))  # Convert port to a string before concatenating
    server.start()
    print("Server started, listening on " + str(port))
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
