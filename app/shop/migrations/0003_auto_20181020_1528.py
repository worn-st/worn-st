# Generated by Django 2.1.2 on 2018-10-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181020_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='proposal',
            new_name='future',
        ),
        migrations.AddField(
            model_name='choice',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='place',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
