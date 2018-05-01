import graphene

from books.schemas.author import AuthorMutation, AuthorQuery, \
    DeleteAuthorMutation
from books.schemas.book import BookQuery, BookMutation
from books.schemas.publisher import PublisherMutation, PublisherQuery, \
    DeletePublisherMutation


class Query(BookQuery, AuthorQuery, PublisherQuery, graphene.ObjectType):
    pass


class Mutation(
    BookMutation, AuthorMutation, PublisherMutation, DeleteAuthorMutation,
    DeletePublisherMutation, graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
