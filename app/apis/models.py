from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=100)
    to_currency = models.CharField(max_length=100)
    ex_rate = models.CharField(max_length=100)

    def __str__(self):
        return "from_currency: " + self.from_currency + " to_currency: " + self.to_currency + " is " + self.ex_rate
