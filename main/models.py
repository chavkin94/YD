from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Расположение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположение'
