from django.contrib import admin
from data.models.author import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Author model.
    """
    list_display = ("author_name",)
    search_fields = ("author_name",)
