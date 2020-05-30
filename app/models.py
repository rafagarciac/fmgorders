from django.db import models

from . import PAYMENT_TYPES_CHOICE, SHOP_TYPES_CHOICES, PAYMENT_CASH, SHOP_FRUIT


class Client(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=150)
    address = models.CharField(verbose_name="Dirección", max_length=300)
    phone_number = models.CharField(verbose_name="Teléfono", max_length=10)

    class Meta:
        ordering = ["name"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

class Order(models.Model):
    create_date = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now=False, auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name="Fecha de actualización", auto_now=True, auto_now_add=False
    )
    payment_type = models.CharField(
        verbose_name="Tipo de pago", max_length=10, choices=PAYMENT_TYPES_CHOICE, default=PAYMENT_CASH
    )
    shop_type = models.CharField(
        verbose_name="Tipo de tienda", max_length=10, choices=SHOP_TYPES_CHOICES, default=SHOP_FRUIT
    )
    total = models.FloatField(verbose_name="Total")
    client = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)

    class Meta:
        ordering = ["create_date"]
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return "{} {} {} - {}".format(self.client, self.shop_type, self.payment_type, str(self.total))
