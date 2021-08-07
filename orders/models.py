from django.db import models
from shop.models import Product
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_verif =models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    # userid = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    usid = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

# class Address(models.Model):
#     customer = models.CharField(max_length=10,unique=True)
#     active = models.BooleanField(default=False)
#     street = models.CharField(max_length=80)
#     city  = models.CharField(max_length=25)
#     pincode = models.CharField(max_length=6)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)

#     class Meta:
#         ordering = ('-created', )

#     def __str__(self):
#         return 'address {}'.format(self.customer)

#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
