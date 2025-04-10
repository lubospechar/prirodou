from django.db import models


class BiologicalCategory(models.Model):
    """
    Model representing a biological category.
    """
    category: str = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Kategorie",
        help_text="Vlož kategorii biologického systému"
    )

    class Meta:
        verbose_name: str = "Kategorie biologického systému"
        verbose_name_plural: str = "Kategorie biologického systému"

    def __str__(self) -> str:
        return self.category