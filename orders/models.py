from django.db import models

# Create your models here.
from products.models import Flowers
from users.models import Buyer, Seller


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCEED, 'Отправлено в обработку'),
        (PAID, 'Оплачено'),
        (PROCEEDED, 'Обрабатывается'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отмена заказа'),
    )

    user = models.ForeignKey(Buyer, blank=True, null=True,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    status = models.CharField(choices=ORDER_STATUS_CHOICES,
                              verbose_name='Статус', max_length=3,
                              default=FORMING)
    from_seller = models.ForeignKey(Seller, blank=True, null=True,
                                    on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ от {self.user.name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              on_delete=models.CASCADE)
    products = models.ManyToManyField(Flowers, verbose_name='Цветочки')
    quantity = models.PositiveIntegerField(verbose_name='Количество',
                                           default=0)

    class Meta:
        verbose_name = 'Что в заказе'
        verbose_name_plural = 'Что в заказах'

    def __str__(self):
        return f'Заказ от {self.order.user.name}'
