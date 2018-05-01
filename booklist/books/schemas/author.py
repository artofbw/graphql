import graphene

from books.models import Author
from books.schemas.types.author import AuthorType


class AuthorQuery:
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(
        AuthorType, id=graphene.ID(),
    )

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_author_by_id(self, info, **kwargs):
        return Author.objects.get(**kwargs)


class CreateAuthor(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    author = graphene.Field(AuthorType)
    created = graphene.Boolean()

    def mutate(self, info, **kwargs):
        author = Author.objects.create(
            first_name=kwargs['first_name'],
            last_name=kwargs['last_name'],
            email=kwargs['email'],
        )
        created = True

        return CreateAuthor(author=author, created=created)


class AuthorMutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    deleted = graphene.Boolean()

    def mutate(self, info, **kwargs):
        Author.objects.get(id=kwargs['id']).delete()

        return DeleteAuthor(deleted=True)


class DeleteAuthorMutation(graphene.ObjectType):
    delete_author = DeleteAuthor.Field()
