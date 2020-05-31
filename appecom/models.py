from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    min_price = models.FloatField(null=True, blank=True)
    max_price = models.FloatField(null=True, blank=True)
    year_since = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    tag = models.BooleanField(default=False)
    rating = models.FloatField(null=True, blank=True)
    cuosines = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catererproduct', kwargs={
            'slug': self.slug
        })
