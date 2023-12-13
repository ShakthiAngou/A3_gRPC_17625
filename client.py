import grpc
import a3_pb2
import a3_pb2_grpc

from datetime import datetime

# Create a Reddit client class
class RedditClient:
    def __init__(self, host='localhost', port=4000):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = a3_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(self, title, text, author_id, subreddit_id):
        post = a3_pb2.Post(
            title=title,
            text=text,
            author_id=author_id,
            subreddit_id=subreddit_id
        )
        response = self.stub.CreatePost(post)
        return response

    def upvote_or_downvote_post(self, entity_id, is_upvote):
        vote = a3_pb2.Vote(entity_id=entity_id, is_upvote=is_upvote)
        response = self.stub.VotePost(vote)
        return response

    def get_post_content(self, post_id):
        post_id_request = a3_pb2.PostID(post_id=post_id)
        response = self.stub.GetPostContent(post_id_request)
        return response

    def create_comment(self, comment_id, post_id, parent_comment_id, author_id, text):
        comment = a3_pb2.Comment(
            comment_id=comment_id,
            post_id=post_id,
            parent_comment_id=parent_comment_id,
            author_id=author_id,
            text=text,
            score=0,
            state=a3_pb2.Comment.NORMAL,
            publication_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Current timestamp
            has_replies=False
        )
        response = self.stub.CreateComment(comment)
        return response

    def upvote_or_downvote_comment(self, entity_id, is_upvote):
        vote = a3_pb2.Vote(entity_id=entity_id, is_upvote=is_upvote)
        response = self.stub.VoteComment(vote)
        return response

    def get_most_upvoted_comments(self, post_id, limit):
        query = a3_pb2.CommentQuery(post_id=post_id, limit=limit)
        response = self.stub.GetMostUpvotedComments(query)
        return response

    def expand_comment_branch(self, comment_id, limit):
        query = a3_pb2.ExpandCommentQuery(comment_id=comment_id, limit=limit)
        response = self.stub.ExpandCommentBranch(query)
        return response

    def monitor_updates(self, post):
        response = self.stub.MonitorUpdates(post)
        for update in response:
            print("Received update:", update)

if __name__ == '__main__':
    client = RedditClient()
    created_post = client.create_post("Sample Title", "Sample Text", "user123", "subreddit456")
    print("Created Post:", created_post)

    upvoted_post = client.upvote_or_downvote_post("123", True)
    print("Upvoted Post:", upvoted_post)

    retrieved_post = client.get_post_content("123")
    print("Retrieved Post Content:", retrieved_post)

    created_comment = client.create_comment("456", "123", "789", "user456", "Sample Comment")
    print("Created Comment:", created_comment)

    upvoted_comment = client.upvote_or_downvote_comment("456", True)
    print("Upvoted Comment:", upvoted_comment)

    most_upvoted_comments = client.get_most_upvoted_comments("123", 5)
    print("Most Upvoted Comments:", most_upvoted_comments)

    expanded_comments = client.expand_comment_branch("456", 2)
    print("Expanded Comment Branch:", expanded_comments)
