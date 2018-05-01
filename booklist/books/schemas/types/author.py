from graphene_django import DjangoObjectType

from books.models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
