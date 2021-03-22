from django.db import models


# Create your models here.
class Expense(models.Model):
    amount = models.FloatField()
    merchant = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)  # enable blank and null values
    category = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
