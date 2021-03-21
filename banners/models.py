from django.db import models

# Create your models here.
class Banner(models.Model):
    description = models.CharField(max_length=150)
    banner = models.ImageField(upload_to="banners")

    def __str__(self):
        return self.description