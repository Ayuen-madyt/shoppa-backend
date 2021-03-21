from django.db import models

# Create your models here.
class ProductFeatured(models.Model):
    description = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='covers')

    class Meta:
        verbose_name_plural = "Products Featured"

    def __str__(self):
        return self.description