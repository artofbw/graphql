import graphene

from books.models import Book
from books.schemas.types.book import BookType


class BookQuery:
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        publication_date = graphene.Date()
        publisher_id = graphene.ID()
        authors = graphene.List(graphene.ID)

    book = graphene.Field(BookType)
    created = graphene.Boolean()

    def mutate(self, info, **kwargs):
        book = Book.objects.create(
            title=kwargs['title'],
            publication_date=kwargs['publication_date'],
            publisher_id=kwargs['publisher_id'],
        )
        book.authors.add(*kwargs['authors'])
        created = True

        return CreateBook(book=book, created=created)


class BookMutation(graphene.ObjectType):
    create_book = CreateBook.Field()
