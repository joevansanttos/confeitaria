from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import CustomUser, Cost, PercentCost, PercentDiscount, PercentLabor
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
        exclude = ['user', 'time']


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


class PercentIngredientUpdateForm(ModelForm):
    class Meta:
        model = PercentIngredient
        fields = ('percent', 'measure')
        exclude = ['product', 'ingredient']


class PercentMaterialForm(ModelForm):
    class Meta:
        model = PercentMaterial
        fields = ('material', 'percent', 'product')

        exclude = ['product']


class PercentMaterialUpdateForm(ModelForm):
    class Meta:
        model = PercentMaterial
        fields = ('percent',)

        exclude = ['product', 'material']


class PercentLaborForm(ModelForm):
    class Meta:
        model = PercentLabor
        fields = ('labor', 'hours', 'time', 'product')

        exclude = ['product']

        labels = {
            "labor": "Mão de Obra"
        }


class PercentLaborUpdateForm(ModelForm):
    class Meta:
        model = PercentLabor
        fields = ('hours', 'time')

        exclude = ['product', 'labor']


class PercentCostForm(ModelForm):
    class Meta:
        model = PercentCost
        fields = ('cost', 'hours', 'time', 'product')

        exclude = ['product']

        labels = {
            "cost": "Custo Fixo"
        }


class PercentCostUpdateForm(ModelForm):
    class Meta:
        model = PercentCost
        fields = ('hours', 'time')

        exclude = ['cost', 'product']


class PercentDiscountForm(ModelForm):
    class Meta:
        model = PercentDiscount
        fields = ('percent',)

        exclude = ['product']


class PercentDiscountUpdateForm(ModelForm):
    class Meta:
        model = PercentDiscount
        fields = ('percent',)

        exclude = ['product']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
        exclude = ['user',
                   'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes']


class ProductFormUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ('another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes')
        exclude = ['user', 'name']


class ProductQuantityFormUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ('quantity',)
        exclude = ['user', 'name',
                   'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'profit']


class ProductNameFormUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
        exclude = ['user', 'quantity',
                   'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'profit']


class ProductProfitFormUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ('profit',)
        exclude = ['user', 'name',
                   'another_expenses', 'incalculable_expenses', 'marketplace_tax', 'taxes', 'quantity']
