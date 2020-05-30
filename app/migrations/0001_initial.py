# Generated by Django 2.2.12 on 2020-05-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('address', models.CharField(max_length=300, verbose_name='Dirección')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('payment_type', models.CharField(choices=[('BIZUM', 'Bizum'), ('TRANSFER', 'Transferencia'), ('CASH', 'Efectivo'), ('CARD', 'Tarjeta'), ('WEB', 'Web')], default='CASH', max_length=10, verbose_name='Tipo de pago')),
                ('shop_type', models.CharField(choices=[('FRUIT', 'Frutería'), ('BAKERY', 'Panadería'), ('BUTCHER', 'Carnicería'), ('FISH', 'Pescadería')], default='FRUIT', max_length=10, verbose_name='Tipo de tienda')),
                ('total', models.FloatField(verbose_name='Total')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='app.Client')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['create_date'],
            },
        ),
    ]