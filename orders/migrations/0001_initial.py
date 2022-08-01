# Generated by Django 4.0.6 on 2022-08-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('status', models.CharField(choices=[('FM', 'Формируется'), ('STP', 'Отправлено в обработку'), ('PD', 'Оплачено'), ('PRD', 'Обрабатывается'), ('RDY', 'Готов к выдаче'), ('CNC', 'Отмена заказа')], default='FM', max_length=3, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.flowers', verbose_name='Цветочки')),
            ],
        ),
    ]