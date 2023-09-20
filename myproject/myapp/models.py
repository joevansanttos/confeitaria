from django.db import models


class Ingredient(models.Model):
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        db_column='quantity', blank=False)
    valor = models.FloatField(db_column='price', blank=False)

    def __str__(self):
        return self.nome


class Material(models.Model):
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        db_column='quantity', blank=False)
    valor = models.FloatField(db_column='price', blank=False)

    def __str__(self):
        return self.nome


class Labor(models.Model):
    salario = models.FloatField(db_column='salary', blank=False)
    horas = models.FloatField(
        db_column='hours', blank=False)
    tempo = models.CharField(db_column='time', max_length=100, blank=False)

    def __str__(self):
        string = str(self.salario / self.horas)
        return string


class Product(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
