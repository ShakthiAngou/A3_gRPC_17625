from client import RedditClient

def retrieve_most_upvoted_reply(api_client: RedditClient):
    post_id = "your_post_id_here"
    limit = 5

    # Retrieve the post content
    post_content = api_client.get_post_content(post_id)
    if post_content:
        # Retrieve most upvoted comments under the post
        most_upvoted_comments = api_client.get_most_upvoted_comments(post_id, limit)

        if most_upvoted_comments.comments:
            # Select the most upvoted comment
            most_upvoted_comment = most_upvoted_comments.comments[0]

            # Expand the most upvoted comment
            expanded_comments = api_client.expand_comment_branch(most_upvoted_comment.comment_id, 2)

            if expanded_comments.comments:
                # Find and return the most upvoted reply under the most upvoted comment
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
