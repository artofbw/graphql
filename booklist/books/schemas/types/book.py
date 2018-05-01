import graphene
from graphene_django import DjangoObjectType

from books.models import Book
from books.schemas.types.author import AuthorType
from books.schemas.types.publisher import PublisherType


class BookType(DjangoObjectType):
    authors = graphene.List(AuthorType)
    publisher = graphene.Field(PublisherType)

    class Meta:
        model = Book

    def resolve_authors(self, *args):
        return self.authors.all()

    def resolve_publisher(self, *args):
        return self.publisher
