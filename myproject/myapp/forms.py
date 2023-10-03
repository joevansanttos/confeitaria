from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import CustomUser, Cost, PercentCost, PercentLabor
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


class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = ('name', 'price', 'hours', 'time')
        exclude = ['user']


class PercentIngredientForm(ModelForm):
    class Meta:
        model = PercentIngredient
        fields = ('ingredient', 'percent', 'measure', 'product')

        labels = {
            "ingredient": "Ingrediente"
        }
        exclude = ['product']


class PercentMaterialForm(ModelForm):
    class Meta:
        model = PercentMaterial
        fields = ('material', 'percent', 'product')

        exclude = ['product']


class PercentLaborForm(ModelForm):
    class Meta:
        model = PercentLabor
        fields = ('labor', 'hours', 'time', 'product')

        exclude = ['product']


class PercentCostForm(ModelForm):
    class Meta:
        model = PercentCost
        fields = ('cost', 'hours', 'time', 'product')

        exclude = ['product']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
<<<<<<< HEAD
        exclude = ['user',
                   'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'quantity', 'profit']


class ProductFormUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ('name',
                  'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'quantity', 'profit')
        exclude = ['user']
=======
        exclude = ['user', 
                  'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'quantity', 'profit']
>>>>>>> 6dcbc09642e41c690a9984380c661c9d800c0800
