from django.db import models

# Create your models here.
from users.models import Seller

COLORS = (
    ('BLUE', 'синий'),
    ('RED', 'красный'),
    ('BLACK', 'черный'),

)


class Flowers(models.Model):
    """Модель цветка"""
    title = models.CharField(max_length=128,
                             verbose_name='Наименование цветка')
    color = models.CharField(choices=COLORS, blank=True,
                             verbose_name='Оттенок', max_length=10)

    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Выставлен на продажу')
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе')
    price = models.DecimalField(verbose_name='стоимость',
                                max_digits=10, decimal_places=2, default=0)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               verbose_name='Продавец', blank=False, null=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return self.title


class ReviewForProduct(models.Model):
    """модель отзыва для товара"""
    name = models.CharField(max_length=64, verbose_name='Имя')
    text = models.CharField(max_length=5000, verbose_name='Текст отзыва')
    product = models.ForeignKey(Flowers, on_delete=models.SET_NULL,
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв о товаре'
        verbose_name_plural = 'Отзывы о товаре'

    def __str__(self):
        return f'Отзыв о "{self.product.title}" от {self.name}'


class ReviewForSeller(models.Model):
    """модель отзыва о продавце"""
    name = models.CharField(max_length=64, verbose_name='Имя')
    text = models.CharField(max_length=5000, verbose_name='Текст отзыва')
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL,
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв о продавце'
        verbose_name_plural = 'Отзывы о продавце'

    def __str__(self):
        return f'Отзыв о "{self.seller.name}" от {self.name}'
