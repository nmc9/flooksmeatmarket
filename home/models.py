from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=12,blank=True, null=True, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    TYPE_CHOICES = (
        ('Beef', 'Beef'),
        ('Poultry', 'Poultry'),
        ('Pork', 'Pork'),
        ('Deli', 'Deli'),
        ('Specialty Meats', 'Specialty Meats'),
        ('Groceries', 'Groceries')
    )
    LOCATION_CHOICES = (
        ('Freezer', 'Freezer'),
        ('Cooler', 'Cooler'),
        ('Snack Rack', 'Snack Rack'),
        ('Pork Case', 'Pork Case'),
        ('Beef/Chicken Case', 'Beef/Chicken Case'),
        ('Cold Meat Case', 'Cold Meat Case'),
        ('Ask Employee', 'Ask Employee')
    )
    type = models.CharField(max_length=20,choices=TYPE_CHOICES, default='Groceries')
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='Ask Employee')
    byPound = models.BooleanField(default=0)  # is it bought by pound

    def get_absolute_url(self):
        return reverse('product:index')

    def __str__(self):
        return self.name


class Basket(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Date = models.DateField(blank=True, null=True)
    PlaceOrder = models.BooleanField(default=0)
    OrderCompleted = models.BooleanField(default=0)
    def get_absolute_url(self):
        return reverse('product:index')

    def __str__(self):
        return "%s basket" % self.User.username


class OrderLine(models.Model):
    quantity = models.DecimalField(max_digits=7, decimal_places=1, validators=[MinValueValidator(Decimal('0.00'))])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return "%s item: %s" % (self.basket, self.product)
