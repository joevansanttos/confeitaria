from django.shortcuts import render, redirect
from .forms import MaterialForm, IngredientForm

from .models import Material, Ingredient


def ingredientList(request):
    ingredients = Ingredient.objects.all()
    return render(request, "ingredient-list.html",
                  {'ingredients': ingredients})


def ingredientCreate(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('ingredient-list')
            except:
                pass
    else:
        form = IngredientForm()
    return render(request, 'ingredient-create.html', {'form': form})


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


def ingredientDelete(request, id):
    ingredient = Ingredient.objects.get(id=id)
    try:
        ingredient.delete()
    except:
        pass
    return redirect('ingredient-list')


def materialList(request):
    materials = Material.objects.all()
    return render(request, "material-list.html", {'materials': materials})


def materialCreate(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('material-list')
            except:
                pass
    else:
        form = MaterialForm()
    return render(request, 'material-create.html', {'form': form})


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


def materialDelete(request, id):
    material = Material.objects.get(id=id)
    try:
        material.delete()
    except:
        pass
    return redirect('material-list')
