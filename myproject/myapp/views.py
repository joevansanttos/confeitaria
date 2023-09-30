import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import MaterialForm, IngredientForm, LaborForm, ProductForm, PercentIngredientForm, PercentMaterialForm
from .models import Material, Ingredient, Labor, Product, PercentIngredient, PercentMaterial
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('myapp:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    current_user = request.user
    return render(request, "profile.html",
                  {'current_user': current_user})


@login_required
def ingredientList(request):
    ingredients = Ingredient.objects.all()
    return render(request, "ingredient-list.html",
                  {'ingredients': ingredients})


def ingredientCreate(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                return redirect('ingredient-list')
            except:
                pass
    else:
        form = IngredientForm()
    return render(request, 'ingredient-create.html', {'form': form})


@login_required
def ingredientUpdate(request, id):
    ingredient = Ingredient.objects.get(id=id)
    form = IngredientForm(
        initial={'name': ingredient.name,
                 'quantity': ingredient.quantity, 'value': ingredient.value}
    )
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/ingredient-list')
            except Exception as e:
                pass
    return render(request, 'ingredient-update.html', {'form': form})


@login_required
def ingredientDelete(request, id):
    ingredient = Ingredient.objects.get(id=id)
    try:
        ingredient.delete()
    except:
        pass
    return redirect('ingredient-list')


@login_required
def percentIngredientList(request):
    percent_ingredients = PercentIngredient.objects.all()
    return render(request, "percent-ingredient-list.html",
                  {'percent_ingredients': percent_ingredients})

@login_required()
def percentIngredientCreate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if not product:
            return redirect('product-list')
        percent_ingredients = PercentIngredient.objects.all()
        form = PercentIngredientForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.product = product
                instance.save()
                form.save()
                model = form.instance
                return HttpResponseRedirect('/product/%d' % id)
            except:
                pass
    else:
        form = PercentIngredientForm()
    return redirect('product-list')


@login_required
def percentIngredientDelete(request, id):
    percent_ingredient = PercentIngredient.objects.get(id=id)
    product = percent_ingredient.product
    product_id = product.id
    try:
        percent_ingredient.delete()
    except:
        pass
    return HttpResponseRedirect('/product/%d' % product_id)


@login_required
def materialList(request):
    materials = Material.objects.all()
    return render(request, "material-list.html", {'materials': materials})


@login_required
def materialCreate(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                return redirect('material-list')
            except:
                pass
    else:
        form = MaterialForm()
    return render(request, 'material-create.html', {'form': form})


@login_required
def materialUpdate(request, id):
    material = Material.objects.get(id=id)
    form = MaterialForm(initial={'title': material.title, 'description': material.description,
                                 'author': material.author, 'year': material.year})
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/material-list')
            except Exception as e:
                pass
    return render(request, 'material-update.html', {'form': form})


@login_required
def materialDelete(request, id):
    material = Material.objects.get(id=id)
    try:
        material.delete()
    except:
        pass
    return redirect('material-list')


@login_required
def percentMaterialList(request):
    percent_materials = PercentMaterial.objects.all()
    return render(request, "percent-material-list.html",
                  {'percent_materials': percent_materials})

@login_required()
def percentMaterialCreate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if not product:
            return redirect('product-list')
        percent_materials = PercentMaterial.objects.all()
        form = PercentMaterialForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.product = product
                instance.save()
                form.save()
                model = form.instance
                return HttpResponseRedirect('/product/%d' % id)
            except:
                pass
    else:
        form = PercentMaterialForm()
    return redirect('product-list')

@login_required
def percentMaterialDelete(request, id):
    percent_material = PercentMaterial.objects.get(id=id)
    product = percent_material.product
    product_id = product.id
    try:
        percent_material.delete()
    except:
        pass
    return HttpResponseRedirect('/product/%d' % product_id)


@login_required
def laborList(request):
    labors = Labor.objects.all()
    return render(request, "labor-list.html", {'labors': labors})


@login_required
def laborCreate(request):
    if request.method == "POST":
        form = LaborForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                return redirect('labor-list')
            except:
                pass
    else:
        form = LaborForm()
    return render(request, 'labor-create.html', {'form': form})


@login_required
def laborUpdate(request, id):
    labor = Labor.objects.get(id=id)
    form = LaborForm(initial={'name': labor.nome, 'salary': labor.salario,
                              'hours': labor.horas, 'time': labor.tempo})
    if request.method == "POST":
        form = LaborForm(request.POST, instance=labor)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/labor-list')
            except Exception as e:
                pass
    return render(request, 'labor-update.html', {'form': form})


@login_required
def laborDelete(request, id):
    labor = Labor.objects.get(id=id)
    try:
        labor.delete()
    except:
        pass
    return redirect('labor-list')


@login_required
def productList(request):
    products = Product.objects.all()

    return render(request, "product-list.html", {'products': products})


@login_required
def productCreate(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                return redirect('product-list')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'product-create.html', {'form': form})


@login_required
def productDelete(request, id):
    product = Product.objects.get(id=id)
    try:
        product.delete()
    except:
        pass
    return redirect('product-list')


@login_required
def product(request, id):
    percent_ingredient_form = PercentIngredientForm()
    percent_material_form = PercentMaterialForm()
    product = Product.objects.get(id=id)
    percent_ingredients = PercentIngredient.objects.all()
    percent_materials = PercentMaterial.objects.all()
    return render(
        request, 'product.html', {
            'product': product,
            'percent_ingredient_form': percent_ingredient_form,
            'percent_material_form': percent_material_form,
            'percent_ingredients': percent_ingredients,
            'percent_materials': percent_materials
        }
    )
