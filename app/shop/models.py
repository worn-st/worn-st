from django.db import models


class Proposal(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of sale')
    usage = models.TextField()


class Choice(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    comment = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
