from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import MaterialForm, IngredientForm, LaborForm, ProductForm
from .models import Material, Ingredient, Labor, Product
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

@login_required
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
def productList(request):
    products = Product.objects.all()
    for product in products:
        ingredientes = product.ingrediente.all()
        for ingrediente in ingredientes:
            print(ingrediente.nome)
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
