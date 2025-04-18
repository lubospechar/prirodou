from django.contrib import admin
from .models.article import Article
from .models.author import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Author model.
    """
    list_display = ("author_name",)
    search_fields = ("author_name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Article model.
    """
    list_display = ("taxon", "citation", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("citation", "authors__author_name", "taxon__taxon_name")
    autocomplete_fields = ("taxon", "authors")
    filter_horizontal = ("authors",)
    fieldsets = (
        (None, {
            "fields": ("taxon", "authors")
        }),
        ("Article Details", {
            "fields": ("citation", "document")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("created_at", "updated_at")