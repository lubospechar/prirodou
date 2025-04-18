from django.db.models import (
    CharField, Model
)


class Author(Model):
    """
    Model representing an Author.
    """

    author_name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.author_name
