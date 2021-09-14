from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField()


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B',
    MEMBERSHIP_SILVER = 'S',
    MEMBERSHIP_GULD = 'G'

    MEMBERSHIP_CHIOCES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GULD, 'Guld'),
    ]
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=220)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHIOCES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P',
    PAYMENT_STATUS_COMPLETE = 'C',
    PAYMENT_STATUS_FAILED = 'F',
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'pending'),
        (PAYMENT_STATUS_COMPLETE, 'complete'),
        (PAYMENT_STATUS_FAILED, 'failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField (
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )
class Adress(models.Model):
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)