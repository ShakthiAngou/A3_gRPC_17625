from client import RedditClient

def retrieve_most_upvoted_reply(api_client: RedditClient):
    client.create_post("Sample Title", "Sample Text", "user123", "subreddit456")
    
    post_id = "1"
    limit = 5

    post_content = api_client.get_post_content(post_id)
    if post_content:
        most_upvoted_comments = api_client.get_most_upvoted_comments(post_id, limit)

        if most_upvoted_comments.comments:
            most_upvoted_comment = most_upvoted_comments.comments[0]
            expanded_comments = api_client.expand_comment_branch(most_upvoted_comment.comment_id, 2)

            if expanded_comments.comments:
                most_upvoted_reply = None
                for comment in expanded_comments.comments:
                    if comment.parent_comment_id == most_upvoted_comment.comment_id:
                        if not most_upvoted_reply or comment.score > most_upvoted_reply.score:
                            most_upvoted_reply = comment

                return most_upvoted_reply
    return None

# Example usage
if __name__ == "__main__":
    client = RedditClient()
    result = retrieve_most_upvoted_reply(client)
    if result:
        print("Most upvoted reply:", result)
    else:
        print("No comments or no replies under the most upvoted comment.")
