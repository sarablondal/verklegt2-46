# Generated by Django 3.0.6 on 2020-05-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consoleimage',
            name='image2',
            field=models.CharField(blank=True, default='', max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consoleimage',
            name='image3',
            field=models.CharField(blank=True, default='', max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consoleimage',
            name='image4',
            field=models.CharField(blank=True, default='', max_length=999),
            preserve_default=False,
        ),
    ]
