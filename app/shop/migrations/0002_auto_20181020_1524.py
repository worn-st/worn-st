# Generated by Django 2.1.2 on 2018-10-20 15:24

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='choices'),
        ),
        migrations.AlterField(
            model_name='future',
            name='date',
            field=models.DateField(verbose_name='date of sale'),
        ),
    ]
