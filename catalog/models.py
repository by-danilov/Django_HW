from users.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец", blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        permissions = [("can_unpublish_product", "Может отменять публикацию продукта"),]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
