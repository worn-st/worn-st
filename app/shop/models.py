from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Future(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default='N', max_length=1)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='purchases')
    value = models.DecimalField(max_digits=6, decimal_places=2,
        verbose_name="Selling price %")
    title = models.CharField(
    	max_length=200,
    	verbose_name='What do you want to buy?')
    date = models.DateField(
    	verbose_name='Date of shipment')
    usage = models.TextField(
    	verbose_name='How whould you use it?')

    def status_text(self):
        if self.status == 'N':
            return 'New'
        return 'Selled'

    def recommended(self):
        if self.choice_set.count() == 0:
            return None

        return Choice.objects.filter(
            future__title__contains=self.title).exclude(future__id=self.pk)

    def main_image(self):
        if not self.choice_set.first:
            return None
        return self.choice_set.first().image


class Choice(models.Model):
    future = models.ForeignKey(Future, on_delete=models.CASCADE)
    comment = models.TextField()
    title = models.CharField(max_length=200, blank=True,
        verbose_name='Brand')
    place = models.CharField(max_length=200, blank=True,
        verbose_name='Where you want to buy?')
    link = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
        verbose_name="Buying price")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = ImageField(upload_to='choices', blank=True)
    selected = models.BooleanField(default=False)

    def final_price(self):
        return self.price * self.future.value / 100
