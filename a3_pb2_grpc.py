# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import a3_pb2 as a3__pb2


class RedditServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/RedditService/CreatePost',
                request_serializer=a3__pb2.Post.SerializeToString,
                response_deserializer=a3__pb2.Post.FromString,
                )
        self.VotePost = channel.unary_unary(
                '/RedditService/VotePost',
                request_serializer=a3__pb2.Vote.SerializeToString,
                response_deserializer=a3__pb2.Post.FromString,
                )
        self.GetPostContent = channel.unary_unary(
                '/RedditService/GetPostContent',
                request_serializer=a3__pb2.PostID.SerializeToString,
                response_deserializer=a3__pb2.Post.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/RedditService/CreateComment',
                request_serializer=a3__pb2.Comment.SerializeToString,
                response_deserializer=a3__pb2.Comment.FromString,
                )
        self.VoteComment = channel.unary_unary(
                '/RedditService/VoteComment',
                request_serializer=a3__pb2.Vote.SerializeToString,
                response_deserializer=a3__pb2.Comment.FromString,
                )
        self.GetMostUpvotedComments = channel.unary_unary(
                '/RedditService/GetMostUpvotedComments',
                request_serializer=a3__pb2.CommentQuery.SerializeToString,
                response_deserializer=a3__pb2.CommentsResponse.FromString,
                )
        self.ExpandCommentBranch = channel.unary_unary(
                '/RedditService/ExpandCommentBranch',
                request_serializer=a3__pb2.ExpandCommentQuery.SerializeToString,
                response_deserializer=a3__pb2.CommentTree.FromString,
                )
        self.MonitorUpdates = channel.unary_stream(
                '/RedditService/MonitorUpdates',
                request_serializer=a3__pb2.Post.SerializeToString,
                response_deserializer=a3__pb2.ScoreUpdates.FromString,
                )


class RedditServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Create a Post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VotePost(self, request, context):
        """Upvote or downvote a Post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostContent(self, request, context):
        """Retrieve Post content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Create a Comment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteComment(self, request, context):
        """Upvote or downvote a Comment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMostUpvotedComments(self, request, context):
        """Retrieve a list of N most upvoted comments under a post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandCommentBranch(self, request, context):
        """Expand a comment branch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MonitorUpdates(self, request, context):
        """Extra credit - Monitor updates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=a3__pb2.Post.FromString,
                    response_serializer=a3__pb2.Post.SerializeToString,
            ),
            'VotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.VotePost,
                    request_deserializer=a3__pb2.Vote.FromString,
                    response_serializer=a3__pb2.Post.SerializeToString,
            ),
            'GetPostContent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostContent,
                    request_deserializer=a3__pb2.PostID.FromString,
                    response_serializer=a3__pb2.Post.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=a3__pb2.Comment.FromString,
                    response_serializer=a3__pb2.Comment.SerializeToString,
            ),
            'VoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteComment,
                    request_deserializer=a3__pb2.Vote.FromString,
                    response_serializer=a3__pb2.Comment.SerializeToString,
            ),
            'GetMostUpvotedComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMostUpvotedComments,
                    request_deserializer=a3__pb2.CommentQuery.FromString,
                    response_serializer=a3__pb2.CommentsResponse.SerializeToString,
            ),
            'ExpandCommentBranch': grpc.unary_unary_rpc_method_handler(
                    servicer.ExpandCommentBranch,
                    request_deserializer=a3__pb2.ExpandCommentQuery.FromString,
                    response_serializer=a3__pb2.CommentTree.SerializeToString,
            ),
            'MonitorUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.MonitorUpdates,
                    request_deserializer=a3__pb2.Post.FromString,
                    response_serializer=a3__pb2.ScoreUpdates.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RedditService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RedditService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/CreatePost',
            a3__pb2.Post.SerializeToString,
            a3__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/VotePost',
            a3__pb2.Vote.SerializeToString,
            a3__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/GetPostContent',
            a3__pb2.PostID.SerializeToString,
            a3__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/CreateComment',
            a3__pb2.Comment.SerializeToString,
            a3__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/VoteComment',
            a3__pb2.Vote.SerializeToString,
            a3__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMostUpvotedComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/GetMostUpvotedComments',
            a3__pb2.CommentQuery.SerializeToString,
            a3__pb2.CommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandCommentBranch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RedditService/ExpandCommentBranch',
            a3__pb2.ExpandCommentQuery.SerializeToString,
            a3__pb2.CommentTree.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MonitorUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/RedditService/MonitorUpdates',
            a3__pb2.Post.SerializeToString,
            a3__pb2.ScoreUpdates.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)