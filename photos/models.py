from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from system.models import Taxon

class Photo(models.Model):
    taxon = models.ForeignKey(Taxon, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(150, 150)],
        format='JPEG',
        options={'quality': 80}
    )

class PhotoDescription(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='descriptions')
    language = models.CharField(max_length=10, choices=[
        ('cs', 'Čeština'),
        ('en', 'English'),
    ])
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktivní")

    class Meta:
        unique_together = ('photo', 'language')

    def __str__(self):
        return f"{self.language.upper()} - {self.title or '[bez názvu]'}"

