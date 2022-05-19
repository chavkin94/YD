# from django.db import models
#
# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=255, blank=True, verbose_name="Наименование категории услуг")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     description = models.TextField(blank=True, verbose_name="Описание категории услуг")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория услуг'
#         verbose_name_plural = 'Категории услуг'
#
#
# class Service(models.Model):
#     name = models.CharField(max_length=255, blank=True, verbose_name="Наименование услуги")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     description = models.TextField(blank=True, verbose_name="Описание услуги")
#     FKServiceCategory = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT,verbose_name="Категория услуг")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Услуга'
#         verbose_name_plural = 'Услуги'
#
#
# class ServiceCustom(models.Model):
#     name = models.CharField(max_length=255, blank=True, verbose_name="Наименование пользовательской услуги")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     description = models.TextField(blank=True, verbose_name="Описание пользовательской услуги")
#     FKServiceCategory = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT,verbose_name="Категория услуг")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Пользовательская услуга'
#         verbose_name_plural = 'Пользовательские услуги'
#
#
# class СMasterAndService(models.Model):
#     price = models.FloatField(blank=True, verbose_name="Стоимость услуги")
#     FKMaster = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, verbose_name="Категория услуг")
#     FKService = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, verbose_name="Категория услуг")
#     FKServiceCustom = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, verbose_name="Категория услуг")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Пользовательская услуга'
#         verbose_name_plural = 'Пользовательские услуги'