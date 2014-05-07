from django.db import models
from django.conf import settings
from os import urandom
from binascii import b2a_hex
from django.utils import timezone
from azuremoon.models import Product, Shipping

def build_uid(this_class):
    return unicode('ca' + b2a_hex(urandom(5)))

class Cart(models.Model):
    cart_id = models.CharField(max_length=20, editable=False, 
        default=build_uid('product'))
    is_submitted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now=True, editable=False)
    checkout_date = models.DateTimeField()
    shipping_place = models.CharField(max_length=200)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2)

class CartItems(models.Model):
	cart_instance = models.ForeignKey(Cart)
	product_id = models.CharField(max_length=20, editable=False)
	name = models.CharField(max_length=200)
	base_price = models.DecimalField(max_digits=5, decimal_places=2)
	quantity = models.IntegerField()
	on_sale = models.BooleanField(default=False)
	collection = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	variation = models.CharField(max_length=200, blank=True)
    variation_price = models.DecimalField(max_digits=5, decimal_places=2, 
    	blank=True)