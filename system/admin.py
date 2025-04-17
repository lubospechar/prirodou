from django.contrib import admin
from .models import BiologicalCategory
from typing import Tuple


@admin.register(BiologicalCategory)
class BiologicalCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the BiologicalCategory model.
    """
    list_display: Tuple[str, ...] = ("category_name",)
    search_fields: Tuple[str, ...] = ("category_name",)