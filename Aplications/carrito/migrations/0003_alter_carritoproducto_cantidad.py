# Generated by Django 4.2.4 on 2023-11-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_carritoproducto_id_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritoproducto',
            name='cantidad',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]