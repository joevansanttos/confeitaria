from django.forms import ModelForm

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
        fields = '__all__'


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class LaborForm(ModelForm):
    class Meta:
        model = Labor
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
