# Generated by Django 3.0.3 on 2020-05-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appecom', '0004_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
