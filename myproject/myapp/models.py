
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
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    sobrenome = models.CharField(db_column='last', max_length=100, blank=False)
    ocupacao = models.CharField(db_column='job', max_length=100, blank=False)
    cidade = models.CharField(db_column='city', max_length=100, blank=False)
    estado = models.CharField(db_column='state', max_length=100, blank=False)
    celular = models.CharField(db_column='phone', max_length=100, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


MEDIDAS_CHOICES = [
    ("KG", "Kg"),
    ("GRAMA", "g"),
]

TEMPO_CHOICES = [
    ("Hora", "Hora"),
    ("Minutos", "Minutos"),
    ("Segundos", "Segundos"),
    ("Dias", "Dias")
]

class Ingredient(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(_("Nome do Item:"), db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        _("Quantidade do Pacote:"), db_column='value', blank=False)
    medidas = models.CharField(_("Medida do Pacote:"), max_length=5, choices=MEDIDAS_CHOICES)
    valor = models.FloatField(_("(R$) Valor do Pacote:"), db_column='price', blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]


class Material(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(_("Nome do Item:"), db_column='name', max_length=100, blank=False)
    quantidade = models.IntegerField(
        _("Quantidade Comprada:"), db_column='quantity', blank=False)
    valor = models.FloatField(_("(R$) Preço do Pacote de Embalagem:"), db_column='price', blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]


class Labor(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(_("Nome do Serviço:"), db_column='name', max_length=100, blank=False)
    salario = models.FloatField(_("Salário Médio:"), db_column='salary', blank=False)
    horas = models.FloatField(
        _("Horas Mensais:"), db_column='hours', blank=False)
    tempo = models.CharField(_("Tempo de Medida:"), max_length=15, choices=TEMPO_CHOICES)

    def __str__(self):
        string = self.nome + " " + str(self.salario / self.horas)
        return string

    class Meta:
        ordering = ["nome"]


class Product(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(db_column='name', max_length=100, blank=False)
    ingrediente = models.ManyToManyField(Ingredient)
    material = models.ManyToManyField(Material)
    trabalho = models.ManyToManyField(Labor)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
