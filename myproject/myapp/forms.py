from django.forms import ModelForm

from .models import Material, Ingredient


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
