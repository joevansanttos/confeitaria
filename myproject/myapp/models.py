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
    name = models.CharField(db_column='name', max_length=100, blank=False)
    last_name = models.CharField(db_column='last', max_length=100, blank=False)
    job = models.CharField(db_column='job', max_length=100, blank=False)
    address = models.CharField(db_column='address', max_length=150, blank=False)
    city = models.CharField(db_column='city', max_length=100, blank=False)
    state = models.CharField(db_column='state', max_length=100, blank=False)
    phone = models.CharField(db_column='phone', max_length=100, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


MEASURES_CHOICES = [
    ("KG", "Kg"),
    ("GRAMAS", "Gramas"),
    ("L", "L"),
    ("mL", "ML"),
    ("UNIDADES", "Unidade(s)")
]

TIME_CHOICES = [
    ("Hora", "Hora"),
    ("Minutos", "Minutos"),
    ("Segundos", "Segundos"),
    ("Dias", "Dias")
]


class Ingredient(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    name = models.CharField(_("Nome do Item:"), db_column='name', max_length=100, blank=False)
    quantity = models.IntegerField(
        _("Quantidade do Pacote:"), db_column='quantity', blank=False)
    measure = models.CharField(_("Medida do Pacote:"), max_length=8, choices=MEASURES_CHOICES)
    price = models.FloatField(_("(R$) Valor do Pacote:"), db_column='price', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Material(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    name = models.CharField(_("Nome do Item:"), db_column='name', max_length=100, blank=False)
    quantity = models.IntegerField(
        _("Quantidade Comprada:"), db_column='quantity', blank=False)
    price = models.FloatField(_("(R$) Preço do Pacote de Embalagem:"), db_column='price', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Labor(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    name = models.CharField(_("Nome do Serviço:"), db_column='name', max_length=100, blank=False)
    salary = models.FloatField(_("Salário Médio:"), db_column='salary', blank=False)
    hours = models.FloatField(
        _("Tempo:"), db_column='hours', blank=False)
    time = models.CharField(_("Medida do Tempo:"), max_length=15, choices=TIME_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Cost(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    name = models.CharField(_("Nome do Custo:"), db_column='name', max_length=100, blank=False)
    price = models.FloatField(_("Preço (R$):"), db_column='price', blank=False)
    hours = models.FloatField(
        _("Horas Mensais:"), db_column='hours', blank=False)
    time = models.CharField(_("Tempo de Medida:"), max_length=15, choices=TIME_CHOICES)

    def __str__(self):
        string = self.name + " " + str(self.price / self.hours)
        return string

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE)
    name = models.CharField(_("Nome do Produto:"), db_column='name', max_length=100, blank=False)
    another_expenses = models.FloatField(_("Outros Custos (R$):"), db_column='another_expenses', blank=True)
    incalculable_expenses = models.FloatField(_("Custos Incalculáveis (R$):"), db_column='incalculable_expenses',
                                              blank=True)
    marketplace_tax = models.FloatField(_("Taxa de Comissão em Marketplace %:"), db_column='marketplace_tax',
                                        blank=True)
    taxes = models.FloatField(_("Impostos %:"), db_column='taxes', blank=True)
    quantity = models.IntegerField(
        _("Quantidade Desejada (UNI):"), db_column='quantity', blank=True)
    profit = models.FloatField(_("Lucro Desejado (R$):"), db_column='profit', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class PercentIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, blank=True, on_delete=models.CASCADE)
    percent = models.IntegerField(
        _("Quantidade Usada:"), db_column='percent', blank=False)
    measure = models.CharField(_("Medida do Pacote:"), max_length=8, choices=MEASURES_CHOICES)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.ingredient.name, self.percent, self.measure)

    class Meta:
        ordering = ["ingredient"]


class PercentMaterial(models.Model):
    material = models.ForeignKey(Material, blank=True, on_delete=models.CASCADE)
    percent = models.IntegerField(
        _("Quantidade Usada:"), db_column='percent', blank=False)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.material.name, self.percent)

    class Meta:
        ordering = ["material"]


class PercentLabor(models.Model):
    labor = models.ForeignKey(Labor, blank=True, on_delete=models.CASCADE)
    hours = models.FloatField(
        _("Horas de Consumo:"), db_column='hours', blank=False)
    time = models.CharField(_("Tempo de Medida:"), max_length=15, choices=TIME_CHOICES)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.labor.name, self.hours)

    class Meta:
        ordering = ["labor"]


class PercentCost(models.Model):
    cost = models.ForeignKey(Cost, blank=True, on_delete=models.CASCADE)
    hours = models.FloatField(
        _("Horas de Consumo:"), db_column='hours', blank=False)
    time = models.CharField(_("Tempo de Medida:"), max_length=15, choices=TIME_CHOICES)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.cost.name, self.hours)

    class Meta:
        ordering = ["cost"]

class PercentDiscount(models.Model):
    percent = models.FloatField(
        _("Porcentagem do Desconto:"), db_column='percent', blank=False)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)

    def __float__(self):
        return self.percent

    class Meta:
        ordering = ["percent"]
