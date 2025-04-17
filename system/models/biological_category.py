from django.db.models import Model, CharField
from django.utils.translation import gettext_lazy as _


class BiologicalCategory(Model):
    """
    Model representing a biological category.
    """

    # Fields
    category_name: str = CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Category name"),
        help_text=_(
            "Enter the name of the biological system category"
        ),  # Lokalizovaný popis pole
    )

    class Meta:
        verbose_name = _("Biological system category")
        verbose_name_plural = _("Biological system categories")

    def __str__(self) -> str:
        return self.category_name
