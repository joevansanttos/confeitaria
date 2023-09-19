from django.db import models


class Ingredient(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    quantity = models.IntegerField(
        db_column='quantity', blank=False, default=1)
    price = models.IntegerField(db_column='price', blank=False, default=1)


class Material(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(
        db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year', blank=False, default=2000)
