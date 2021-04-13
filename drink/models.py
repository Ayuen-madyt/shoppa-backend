from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Drink(models.Model):
    CATEGORIES = (
        ('Wines and Spirits', 'Wines and Spirits'),
        ('Energy Drinks', 'Energy Drinks'),
        ('Soft Drinks', 'Soft Drinks'),
        ('Water', 'Water'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=150)
    variation = models.CharField(max_length=150, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    cover_picture = models.ImageField(upload_to='covers')
    category = models.CharField(max_length=150, choices=CATEGORIES)
    brand = models.CharField(max_length=150, null=True, blank=True, help_text="input a company,brand or group that made the product")
    price = models.PositiveIntegerField()
    previous_price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = "Drinks"

    def __str__(self):
        return self.name


class Order(models.Model):
    DELIVERY_METHODS = (
        ('Door delivery', 'Door delivery'),
        ('Pick up station', 'Pick up station'),
    )
    PAYMENT_METHODS = (
        ('Payment on delivery', 'Payment on delivery'),
        ('Pay before delivery', 'Pay before delivery'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, help_text="*Do not fill this field*")
    order_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=150,help_text="*Do not fill this field*", null=True, blank=True)
    location = models.CharField(max_length=150, help_text="Choose a town or city you live in: *Do not fill this filed*")
    area = models.CharField(max_length=150, help_text="Choose correct location you live in that town: *Do not fill this filed*")
    delivery = models.CharField(max_length=150, choices=DELIVERY_METHODS, help_text="*Do not fill this field*")
    payment = models.CharField(max_length=150,choices=PAYMENT_METHODS, null=True, blank=True)
    delivered = models.BooleanField(null=True, blank=True,default=False, help_text="*Fill this field when the delivery has been made*")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    class Meta:  
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'{self.drink} order by {self.customer}, Delivered: {self.delivered}'
    
