from django.db import models

# https://snipp.ru/handbk/geo-russia
class LocationDistrict(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Федеральный округ'
            verbose_name_plural = 'Федеральные округа'


class LocationRegions(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    district = models.ForeignKey(LocationDistrict, on_delete=models.PROTECT, verbose_name='Федеральный округ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class LocationСity(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    region = models.ForeignKey(LocationRegions, on_delete=models.PROTECT, verbose_name='Регион')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Location(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Расположение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположение'


class test(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Расположение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'test'
