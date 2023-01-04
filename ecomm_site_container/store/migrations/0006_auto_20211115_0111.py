# Generated by Django 3.2.8 on 2021-11-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_cart_is_empty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_empty',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]