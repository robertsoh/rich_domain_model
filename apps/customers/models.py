
from django.db import models


class CustomerORM(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    status = models.IntegerField()
    status_expiration_date = models.DateTimeField(blank=True, null=True)
    money_spent = models.DecimalField(decimal_places=2, max_digits=20)
