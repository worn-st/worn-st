# Generated by Django 2.1.2 on 2018-10-20 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20181020_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='future',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='future',
            name='status',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='future',
            name='value',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=6, verbose_name='Selling price %'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='Where you want to buy?'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buying price'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='future',
            name='date',
            field=models.DateField(verbose_name='Date of shipment'),
        ),
        migrations.AlterField(
            model_name='future',
            name='title',
            field=models.CharField(max_length=200, verbose_name='What do you want to buy?'),
        ),
        migrations.AlterField(
            model_name='future',
            name='usage',
            field=models.TextField(verbose_name='How whould you use it?'),
        ),
    ]
