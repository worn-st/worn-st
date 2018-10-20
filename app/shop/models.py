from django.db import models
from django.contrib.auth.models import User


class Future(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField('date of sale')
    usage = models.TextField()


class Choice(models.Model):
    proposal = models.ForeignKey(Future, on_delete=models.CASCADE)
    comment = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)