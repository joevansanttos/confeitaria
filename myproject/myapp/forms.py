from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _

from .models import CustomUser
from .models import Material, Ingredient, Labor, Product, PercentIngredient, PercentMaterial


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
        fields = ('name', 'quantity', 'measure', 'price')
        exclude = ['user']


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ('name', 'quantity', 'price')
        exclude = ['user']


class LaborForm(ModelForm):
    class Meta:
        model = Labor
        fields = ('name', 'salary', 'hours', 'time')
        exclude = ['user']


class PercentIngredientForm(ModelForm):
    class Meta:
        model = PercentIngredient
        fields = ('ingredient', 'percent', 'measure')

        labels = {
            "ingredient": "Ingrediente"
        }


class PercentMaterialForm(ModelForm):
    class Meta:
        model = PercentMaterial
        fields = ('material', 'percent')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'percent_ingredients', 'percent_materials', 'labor',
                  'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'quantity', 'profit' )
        exclude = ['user']

    labels = {
        "percent_ingredients": "Quant. Usada do Ingrediente"
    }

    percent_ingredients = ModelMultipleChoiceField(
        queryset=PercentIngredient.objects.all(),
        widget=CheckboxSelectMultiple
    )

    percent_materials = ModelMultipleChoiceField(
        queryset=PercentMaterial.objects.all(),
        widget=CheckboxSelectMultiple
    )
