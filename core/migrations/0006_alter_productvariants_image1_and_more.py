# Generated by Django 5.1.7 on 2025-03-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_values_product_attributes_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariants',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
