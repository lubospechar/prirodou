from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import BiologicalCategory, Taxon
from typing import Tuple


@admin.register(BiologicalCategory)
class BiologicalCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the BiologicalCategory model.
    """

    list_display: Tuple[str, ...] = ("category_name",)
    search_fields: Tuple[str, ...] = ("category_name",)


@admin.register(Taxon)
class TaxonAdmin(MPTTModelAdmin):
    """
    Customized admin for Taxon model displaying additional annotations and leveraging type hints.
    """

    list_display: Tuple[str, ...] = (
        "taxon_name",
        "category",
        "parent_name",
        "children_count",
    )
    search_fields: Tuple[str, ...] = ("taxon_name",)
    list_filter: Tuple[str, ...] = ("category",)
    mptt_level_indent: int = 20
    fields: Tuple[str, ...] = ("taxon_name", "category", "parent")
    save_on_top: bool = True

    def parent_name(self, obj) -> str:
        return obj.parent.taxon_name if obj.parent else "-"

    parent_name.short_description = "Parent Name"

    def children_count(self, obj) -> int:
        return obj.children.count()

    children_count.short_description = "Children Count"
    children_count.admin_order_field = "children__count"
