from django.db.models import CharField, ForeignKey
from django.db.models import PROTECT
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from system.models import BiologicalCategory


class Taxon(MPTTModel):
    taxon_name = CharField(verbose_name=_("taxon_name"), max_length=255)

    category = ForeignKey(
        BiologicalCategory, verbose_name=_("category"), on_delete=PROTECT, related_name="taxon"
    )
    parent = TreeForeignKey(
        "self",
        verbose_name=_("parent"),
        on_delete=PROTECT,
        null=True,
        blank=True,
        related_name="children",
    )

    class MPTTMeta:
        order_insertion_by = ["taxon_name"]

    def __str__(self) -> str:
        return self.taxon_name
