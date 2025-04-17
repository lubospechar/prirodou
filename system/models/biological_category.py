from django.db.models import Model, CharField


class BiologicalCategory(Model):
    """
    Model representing a biological category.
    """

    # Fields
    category_name: str = CharField(
        max_length=255,
        unique=True,
        verbose_name="Category name",
        help_text="Enter the name of the biological system category"
    )

    class Meta:
        # Directly define verbose names in Meta
        verbose_name = "Biological system category"
        verbose_name_plural = "Biological system categories"

    def __str__(self) -> str:
        return self.category_name


