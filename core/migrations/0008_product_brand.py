# Generated by Django 5.1.7 on 2025-03-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_category_product_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
