from django.forms import ModelForm, forms
from .models import Material, Ingredient, Labor, Product

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ('nome', 'quantidade', 'medidas', 'valor')
        exclude = ['user']


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ('nome', 'quantidade', 'valor')
        exclude = ['user']


class LaborForm(ModelForm):
    class Meta:
        model = Labor
        fields = ('nome', 'salario', 'horas', 'tempo')
        exclude = ['user']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('nome', 'ingrediente', 'material', 'trabalho')
        exclude = ['user']
