# Generated by Django 3.0.3 on 2020-05-20 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appecom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
