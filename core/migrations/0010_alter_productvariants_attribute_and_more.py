# Generated by Django 5.1.7 on 2025-03-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_productsizeoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariants',
            name='attribute',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='extra_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
