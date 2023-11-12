# Generated by Django 4.2.4 on 2023-10-22 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('Usuario_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['fecha_pedido'],
            },
        ),
    ]
