from django.db.models import (
    CharField,
    DateTimeField,
    FileField,
    ForeignKey,
    ManyToManyField,
    CASCADE, Model
)

from data.models.author import Author
from system.models import Taxon


class Article(Model):
    """
    Model representing an Article linked to a Taxon and multiple Authors.
    """

    taxon = ForeignKey(
        Taxon,
        on_delete=CASCADE,
        related_name="articles"
    )
    authors = ManyToManyField(
        Author,
        related_name="articles",
        blank=True
    )
    citation = CharField(
        max_length=255,
        blank=True,
        null=True
    )
    document = FileField(
        upload_to="data/articles/documents/"
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        author_names = ", ".join(author.author_name for author in self.authors.all())
        return f"Article related to {self.taxon.taxon_name} by {author_names or 'Unknown Authors'}"