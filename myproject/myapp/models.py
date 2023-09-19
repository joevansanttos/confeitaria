from django.db import models


class Ingredient(models.Model):
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        db_column='quantity', blank=False)
    valor = models.FloatField(db_column='price', blank=False)


class Material(models.Model):
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        db_column='quantity', blank=False)
    valor = models.FloatField(db_column='price', blank=False)


class Labor(models.Model):
    salario = models.FloatField(db_column='salary', blank=False)
    horas = models.FloatField(
        db_column='hours', blank=False)
    tempo = models.CharField(db_column='time', max_length=100, blank=False)
