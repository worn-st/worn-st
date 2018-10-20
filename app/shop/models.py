from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Future(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
    	max_length=200, verbose_name='What do you want to buy?')
    date = models.DateField(
    	verbose_name='Date of shipment')
    usage = models.TextField(
    	verbose_name='How whould you use it?')


class Choice(models.Model):
    future = models.ForeignKey(Future, on_delete=models.CASCADE)
    comment = models.TextField()
    title = models.CharField(max_length=200, blank=True)
    place = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = ImageField(upload_to='choices', blank=True)