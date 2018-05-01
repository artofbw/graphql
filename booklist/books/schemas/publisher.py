import graphene

from books.models import Publisher
from books.schemas.types.publisher import PublisherType


class PublisherQuery:
    all_publishers = graphene.List(PublisherType)
    publisher_by_id = graphene.Field(
        PublisherType, id=graphene.ID(),
    )

    def resolve_all_publishers(self, info, **kwargs):
        return Publisher.objects.all()

    def resolve_publisher_by_id(self, info, **kwargs):
        return Publisher.objects.get(**kwargs)


class CreatePublisher(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        city = graphene.String()
        state_province = graphene.String()
        country = graphene.String()
        website = graphene.String()

    publisher = graphene.Field(PublisherType)
    created = graphene.Boolean()

    def mutate(self, info, **kwargs):
        publisher = Publisher.objects.create(
            name=kwargs['name'],
            address=kwargs['address'],
            city=kwargs['city'],
            state_province=kwargs['state_province'],
            country=kwargs['country'],
            website=kwargs['website'],
        )
        created = True

        return CreatePublisher(publisher=publisher, created=created)


class PublisherMutation(graphene.ObjectType):
    create_publisher = CreatePublisher.Field()


class DeletePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    deleted = graphene.Boolean()

    def mutate(self, info, **kwargs):
        Publisher.objects.get(id=kwargs['id']).delete()

        return DeletePublisher(deleted=True)


class DeletePublisherMutation(graphene.ObjectType):
    delete_publisher = DeletePublisher.Field()
