# Generated by Django 3.0.3 on 2020-05-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appecom', '0003_auto_20200520_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
