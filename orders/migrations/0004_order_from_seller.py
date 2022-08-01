# Generated by Django 4.0.6 on 2022-08-01 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('orders', '0003_remove_orderitem_product_orderitem_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='from_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.seller'),
        ),
    ]