import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages #import messages


from .forms import MaterialForm, IngredientForm, LaborForm, PercentCostUpdateForm, PercentDiscountForm, \
    PercentIngredientUpdateForm, PercentLaborUpdateForm, PercentMaterialUpdateForm, ProductForm, PercentIngredientForm, \
    PercentMaterialForm, \
    CostForm, PercentLaborForm, PercentCostForm, ProductFormUpdate, ProductProfitFormUpdate, ProductQuantityFormUpdate, \
    PercentDiscountUpdateForm
from .models import TIME_CHOICES, Material, Ingredient, Labor, PercentDiscount, Product, PercentIngredient, PercentMaterial, Cost, PercentLabor, \
    PercentCost
from .forms import CustomUserCreationForm
import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    return render(request, "dashboard.html")


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
    current_user = request.user
    ingredients = current_user.ingredient_set.all()
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
                messages.success(request, "Ingrediente " + instance.name + " Adicionado!")
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
                 'quantity': ingredient.quantity, 'price': ingredient.price, 'measure': ingredient.measure}
    )
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Ingrediente " + ingredient.name + " Atualizado!!!")
                return redirect('/ingredient-list')
            except Exception as e:
                pass
    return render(request, 'ingredient-update.html', {'form': form})


@login_required
def ingredientDelete(request, id):
    ingredient = Ingredient.objects.get(id=id)
    try:
        ingredient.delete()
        messages.error(request, "Ingrediente " + ingredient.name + " excluído!!!")
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
        print("percent")
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
def percentIngredientUpdate(request, id):
    percentIngredient = PercentIngredient.objects.get(id=id)
    form = PercentIngredientUpdateForm(initial={'percent': percentIngredient.percent, 'measure': percentIngredient.measure, 'ingredient': percentIngredient.ingredient, 'product': percentIngredient.product})
    if request.method == "POST":
        form = PercentIngredientUpdateForm(request.POST, instance=percentIngredient)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Porcentagem do ingrediente " + percentIngredient.ingredient.name + " Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % percentIngredient.product.pk)
            except Exception as e:
                pass
    return render(request, 'percent-ingredient-update.html', {'form': form})


@login_required
def materialList(request):
    current_user = request.user
    materials = current_user.material_set.all()
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
                messages.success(request, "Material " + instance.name + " Adicionado!")
                return redirect('material-list')
            except:
                pass
    else:
        form = MaterialForm()
    return render(request, 'material-create.html', {'form': form})


@login_required
def materialUpdate(request, id):
    material = Material.objects.get(id=id)
    form = MaterialForm(initial={'name': material.name, 'quantity': material.quantity,
                                 'price': material.price})
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Material " + material.name + " Atualizado!!!")
                return redirect('/material-list')
            except Exception as e:
                pass
    return render(request, 'material-update.html', {'form': form})


@login_required
def materialDelete(request, id):
    material = Material.objects.get(id=id)
    try:
        material.delete()
        messages.error(request, "Material " + material.name + " excluído!!!")
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
def percentMaterialUpdate(request, id):
    percentMaterial = PercentMaterial.objects.get(id=id)
    form = PercentMaterialUpdateForm(initial={'percent': percentMaterial.percent, 'material': percentMaterial.material, 'product': percentMaterial.product})
    if request.method == "POST":
        form = PercentMaterialUpdateForm(request.POST, instance=percentMaterial)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Porcentagem do Material " + percentMaterial.material.name + " Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % percentMaterial.product.pk)
            except Exception as e:
                pass
    return render(request, 'percent-material-update.html', {'form': form})


@login_required
def laborList(request):
    current_user = request.user
    labors = current_user.labor_set.all()
    return render(request, "labor-list.html", {'labors': labors})


@login_required
def laborCreate(request):
    if request.method == "POST":
        form = LaborForm(request.POST)
        if form.is_valid():
            try:
                form.instance.time = 'Hora'
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                messages.success(request, "Mão de Obra " + instance.name + " Adicionada!")
                return redirect('labor-list')
            except:
                pass
    else:
        form = LaborForm()
    return render(request, 'labor-create.html', {'form': form})


@login_required
def laborUpdate(request, id):
    labor = Labor.objects.get(id=id)
    form = LaborForm(initial={'name': labor.name, 'salary': labor.salary,
                              'hours': labor.hours, 'time': labor.time})
    if request.method == "POST":
        form = LaborForm(request.POST, instance=labor)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Mão de Obra " + labor.name + " Atualizado!!!")
                return redirect('/labor-list')
            except Exception as e:
                pass
    return render(request, 'labor-update.html', {'form': form})


@login_required
def laborDelete(request, id):
    labor = Labor.objects.get(id=id)
    try:
        labor.delete()
        messages.error(request, "Mão de Obra " + labor.name + " excluído!!!")
    except:
        pass
    return redirect('labor-list')


@login_required
def percentLaborList(request):
    percent_labors = PercentLabor.objects.all()
    return render(request, "percent-labor-list.html",
                  {'percent_labors': percent_labors})


@login_required()
def percentLaborCreate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if not product:
            return redirect('product-list')
        percent_labors = PercentLabor.objects.all()
        form = PercentLaborForm(request.POST)
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
        form = PercentLaborForm()
    return redirect('product-list')


@login_required
def percentLaborDelete(request, id):
    percent_labor = PercentLabor.objects.get(id=id)
    product = percent_labor.product
    product_id = product.id
    try:
        percent_labor.delete()
    except:
        pass
    return HttpResponseRedirect('/product/%d' % product_id)

@login_required
def percentLaborUpdate(request, id):
    percentLabor = PercentLabor.objects.get(id=id)
    form = PercentLaborUpdateForm(initial={'time': percentLabor.time, 'hours': percentLabor.hours, 'labor': percentLabor.labor, 'product': percentLabor.product})
    if request.method == "POST":
        form = PercentLaborUpdateForm(request.POST, instance=percentLabor)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Porcentagem do Material " + percentLabor.labor.name + " Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % percentLabor.product.pk)
            except Exception as e:
                pass
    return render(request, 'percent-labor-update.html', {'form': form})


@login_required
def costList(request):
    current_user = request.user
    costs = current_user.cost_set.all()
    return render(request, "cost-list.html",
                  {'costs': costs})


def costCreate(request):
    if request.method == "POST":
        form = CostForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save()
                model = form.instance
                messages.success(request, "Custo Fixo " + instance.name + " Adicionado!")
                return redirect('cost-list')
            except:
                pass
    else:
        form = CostForm()
    return render(request, 'cost-create.html', {'form': form})


@login_required
def costUpdate(request, id):
    cost = Cost.objects.get(id=id)
    form = CostForm(
        initial={'name': cost.name,
                 'price': cost.price, 'hours': cost.hours, 'time': cost.time}
    )
    if request.method == "POST":
        form = CostForm(request.POST, instance=cost)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Custo Fixo " + cost.name + " Atualizado!!!")
                return redirect('/cost-list')
            except Exception as e:
                pass
    return render(request, 'cost-update.html', {'form': form})


@login_required
def costDelete(request, id):
    cost = Cost.objects.get(id=id)
    try:
        cost.delete()
        messages.error(request, "Custo Fixo " + cost.name + " excluído!!!")
    except:
        pass
    return redirect('cost-list')


@login_required
def percentCostList(request):
    percent_costs = PercentCost.objects.all()
    return render(request, "percent-cost-list.html",
                  {'percent_costs': percent_costs})


@login_required()
def percentCostCreate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if not product:
            return redirect('product-list')
        percent_costs = PercentCost.objects.all()
        form = PercentCostForm(request.POST)
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
        form = PercentCostForm()
    return redirect('product-list')


@login_required
def percentCostDelete(request, id):
    percent_cost = PercentCost.objects.get(id=id)
    product = percent_cost.product
    product_id = product.id
    try:
        percent_cost.delete()
    except:
        pass
    return HttpResponseRedirect('/product/%d' % product_id)

@login_required
def percentCostUpdate(request, id):
    percentCost = PercentCost.objects.get(id=id)
    form = PercentCostUpdateForm(initial={'time': percentCost.time, 'hours': percentCost.hours, 'cost': percentCost.cost, 'product': percentCost.product})
    if request.method == "POST":
        form = PercentCostUpdateForm(request.POST, instance=percentCost)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Porcentagem do Custo " + percentCost.cost.name + " Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % percentCost.product.pk)
            except Exception as e:
                pass
    return render(request, 'percent-cost-update.html', {'form': form})


@login_required
def percentDiscountList(request):
    percent_discounts = PercentDiscount.objects.all()
    return render(request, "percent-discount-list.html",
                  {'percent_discounts': percent_discounts})


@login_required()
def percentDiscountCreate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if not product:
            return redirect('product-list')
        form = PercentDiscountForm(request.POST)
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
        form = PercentDiscountForm()
    return redirect('product-list')


@login_required
def percentDiscountDelete(request, id):
    percent_discount = PercentDiscount.objects.get(id=id)
    product = percent_discount.product
    product_id = product.id
    try:
        percent_discount.delete()
    except:
        pass
    return HttpResponseRedirect('/product/%d' % product_id)

@login_required
def percentDiscountUpdate(request, id):
    percentDiscount = PercentDiscount.objects.get(id=id)
    form = PercentDiscountUpdateForm(initial={'percent': percentDiscount.percent, 'product': percentDiscount.product})
    if request.method == "POST":
        form = PercentDiscountUpdateForm(request.POST, instance=percentDiscount)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                print(percentDiscount.product.pk)
                messages.info(request, "Porcentagem do Custo " + percentDiscount.percent + "% Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % percentDiscount.product.pk)
            except Exception as e:
                pass
    return render(request, 'percent-discount-update.html', {'form': form})



@login_required
def productList(request):
    current_user = request.user
    products = current_user.product_set.all()
    for product in products:
        (price_unity, all_total_costs, total_ingredients, total_materials, total_labors,
         totals_costs) = generate_price_unity(product)
        product.price_unity = price_unity

    return render(request, "product-list.html", {'products': products})


@login_required
def productCreate(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print("is valido")
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.another_expenses = 0
                instance.incalculable_expenses = 0
                instance.marketplace_tax = 0
                instance.taxes = 0
                instance.quantity = 0
                instance.profit = 0
                instance.save()
                form.save()
                model = form.instance
                messages.success(request, "Produto " + instance.name + " Adicionado!")
                return HttpResponseRedirect('/product/%d' % model.id)
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'product-create.html', {'form': form})

@login_required
def productUpdate(request, id):
    product = Product.objects.get(id=id)
    form = ProductFormUpdate(
        initial={'name': product.name,
                 'another_expenses': product.another_expenses, 'incalculable_expenses': product.incalculable_expenses,
                 'marketplace_tax': product.marketplace_tax, 'taxes': product.taxes,
                 'quantity': product.quantity, 'profit': product.profit}
    )
    if request.method == "POST":
        form = ProductFormUpdate(request.POST, instance=product)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                messages.info(request, "Produto " + product.name + " Atualizado!!!")
                return HttpResponseRedirect('/product/%d' % id)
            except Exception as e:
                pass
    return render(request, 'product-update.html', {'form': form})

@login_required
def productQuantityUpdate(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductQuantityFormUpdate(request.POST, instance=product)
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
        form = ProductQuantityFormUpdate()
    return redirect('product-list')

@login_required
def productProfitUpdate(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductProfitFormUpdate(request.POST, instance=product)
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
        form = ProductProfitFormUpdate()
    return redirect('product-list')


@login_required
def productDelete(request, id):
    product = Product.objects.get(id=id)
    try:
        product.delete()
        messages.error(request, "Produto " + product.name + " excluído!!!")
    except:
        pass
    return redirect('product-list')


@login_required
def product(request, id):
    product = Product.objects.get(id=id)
    percent_ingredient_form = PercentIngredientForm()
    percent_ingredient_update_form = PercentIngredientUpdateForm()
    current_user = request.user
    percent_ingredient_form.fields["ingredient"].queryset = Ingredient.objects.filter(user_id=current_user.id)
    percent_material_form = PercentMaterialForm()
    percent_material_form.fields["material"].queryset = Material.objects.filter(user_id=current_user.id)
    percent_labor_form = PercentLaborForm()
    percent_labor_form.fields["labor"].queryset = Labor.objects.filter(user_id=current_user.id)
    percent_cost_form = PercentCostForm()
    percent_cost_form.fields["cost"].queryset = Cost.objects.filter(user_id=current_user.id)
    percent_discount_form = PercentDiscountForm()
    product_quantity_update_form = ProductQuantityFormUpdate()
    product_profit_update_form = ProductProfitFormUpdate()
    percent_ingredients = product.percentingredient_set.all()
    percent_materials = product.percentmaterial_set.all()
    percent_labors = product.percentlabor_set.all()
    percent_costs =product.percentcost_set.all()
    percent_discounts =product.percentdiscount_set.all()
    (price_unity, all_total_costs, total_ingredients, total_materials, total_labors,
     totals_costs) = generate_price_unity(product)
    roi = (product.profit * all_total_costs) / 100
    cmv = (total_ingredients + total_materials) / (round(price_unity, 2) * product.quantity)



    return render(
        request, 'product.html', {
            'product': product,
            'percent_ingredient_form': percent_ingredient_form,
            'percent_ingredient_update_form': percent_ingredient_update_form,
            'percent_material_form': percent_material_form,
            'percent_labor_form': percent_labor_form,
            'percent_cost_form': percent_cost_form,
            'percent_discount_form':  percent_discount_form,
            'product_quantity_update_form': product_quantity_update_form,
            'product_profit_update_form': product_profit_update_form,
            'percent_ingredients': percent_ingredients,
            'percent_materials': percent_materials,
            'percent_labors': percent_labors,
            'percent_costs': percent_costs,
            'percent_discounts': percent_discounts,
            'price_unity': round(price_unity, 2),
            'all_total_costs': all_total_costs,
            'roi': round(roi, 2),
            'total_ingredients': total_ingredients,
            'total_materials': total_materials,
            'total_labors': total_labors,
            'total_costs': totals_costs,
            'cmv': round(cmv, 2)
        }
    )


def generate_price_unity(product):
    percent_ingredients = product.percentingredient_set.all()
    percent_materials = product.percentmaterial_set.all()
    percent_labors = product.percentlabor_set.all()
    percent_costs =product.percentcost_set.all()
    total_ingredients = calc_ingredients_value(percent_ingredients)
    total_materials = calc_materials_value(percent_materials)
    total_labors = calc_labors_value(percent_labors)
    total_costs = calc_costs_value(percent_costs)
    incalculable = product.incalculable_expenses / 100 * total_ingredients
    total_cost = total_ingredients + total_materials + total_labors + total_costs + product.another_expenses + incalculable + product.profit
    machine = product.taxes / 100 if product.taxes != 0 else 0
    comission = product.marketplace_tax / 100 if product.marketplace_tax != 0 else 0
    taxes_market = (total_cost / (1 - (comission + machine)) - total_cost)
    comission_tax = taxes_market * (comission / (comission + machine)) if comission != 0 else 0
    comission_machine = taxes_market * (machine / (comission + machine)) if machine != 0 else 0
    all_total_costs = total_ingredients + total_materials + total_labors + total_costs + product.another_expenses + incalculable + comission_tax + comission_machine
    price_unity = (all_total_costs + product.profit) / product.quantity \
        if product.profit != 0 and product.quantity != 0 else 0
    return (round(price_unity, 2), round(all_total_costs, 2), round(total_ingredients, 2), round(total_materials, 2),
            round(total_labors, 2), round(total_costs, 2))


def calc_ingredients_value(percent_ingredients):
    calc_ingredients = 0
    for percent_ingredient in percent_ingredients:

        if percent_ingredient.measure != percent_ingredient.ingredient.measure:
            calc_ingredient = (percent_ingredient.percent / (percent_ingredient.ingredient.quantity * 1000)) * \
                              percent_ingredient.ingredient.price
        else:
            calc_ingredient = (percent_ingredient.percent / percent_ingredient.ingredient.quantity) * \
                              percent_ingredient.ingredient.price

        calc_ingredients = calc_ingredients + round(calc_ingredient, 2)
    return calc_ingredients


def calc_materials_value(percent_materials):
    calc_materials = 0
    for percent_material in percent_materials:
        calc_material = (percent_material.percent / percent_material.material.quantity) * \
                        percent_material.material.price
        calc_materials = calc_materials + round(calc_material, 2)
    return calc_materials


def calc_labors_value(percent_labors):
    calc_labors = 0
    for percent_labor in percent_labors:
        calc_labor = percent_labor.hours * (percent_labor.labor.salary / percent_labor.labor.hours)
        calc_labors = calc_labors + round(calc_labor, 2)
    return calc_labors


def calc_costs_value(percent_costs):
    calc_costs = 0
    for percent_cost in percent_costs:
        calc_cost = percent_cost.hours * (percent_cost.cost.price / percent_cost.cost.hours)
        calc_costs = calc_costs + round(calc_cost, 2)
    return calc_costs
