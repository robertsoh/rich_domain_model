
from django.db import models


class ORMCustomer(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    status = models.IntegerField()
    status_expiration_date = models.DateTimeField(blank=True, null=True)
    money_spent = models.DecimalField(decimal_places=2, max_digits=20)
