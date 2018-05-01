from graphene_django import DjangoObjectType

from books.models import Publisher


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
