# Generated by Django 4.0.6 on 2022-08-01 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_buyer_options_alter_role_options_and_more'),
        ('products', '0004_flowers_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.seller', verbose_name='Продавец'),
        ),
    ]
