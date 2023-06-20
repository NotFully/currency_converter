from django.db import models


class ExchangeRate(models.Model):
    currency_code = models.CharField(max_length=3)
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'{self.currency_code} ({self.date})'
