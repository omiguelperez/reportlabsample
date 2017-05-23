from django.db import models


class Customer(models.Model):
    identity_card = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
