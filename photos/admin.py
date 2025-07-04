from django.contrib import admin
from django.utils.html import format_html
from .models import Photo, PhotoDescription


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Photo model.
    """
    list_display = ('taxon', 'thumbnail_preview')
    search_fields = ('taxon__taxon_name',)
    readonly_fields = ('thumbnail_preview',)
    fields = ('taxon', 'image', 'thumbnail_preview')

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="150" height="150" />', obj.thumbnail.url)
        return "No image available"
    thumbnail_preview.short_description = "Thumbnail Preview"


@admin.register(PhotoDescription)
class PhotoDescriptionAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the PhotoDescription model.
    """
    list_display = ('photo', 'language', 'title', 'is_active')
    list_filter = ('language', 'is_active')
    search_fields = ('title', 'description', 'photo__taxon__taxon_name')
    autocomplete_fields = ('photo',)
    fieldsets = (
        (None, {
            'fields': ('photo', 'language', 'is_active'),
        }),
        ('Content', {
            'fields': ('title', 'description'),
        }),
    )
