from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    pizzaname = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 100)
    price = models.FloatField()

class CustomerModel(models.Model):
    userid = models.CharField(max_length = 10)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    confirm_password=models.CharField(max_length=10)

class OrderModel(models.Model):
    username = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    ordereditems = models.CharField(max_length = 10)
    orders_status = models.CharField(max_length = 10)
