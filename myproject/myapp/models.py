from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
