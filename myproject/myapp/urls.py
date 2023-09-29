from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('ingredient-list', views.ingredientList, name='ingredient-list'),
    path('ingredient-create', views.ingredientCreate,
         name='ingredient-create'),
    path('ingredient-update/<int:id>',
         views.ingredientUpdate, name='ingredient-update'),
    path('ingredient-delete/<int:id>',
         views.ingredientDelete, name='ingredient-delete'),
    path('percent-ingredient-list', views.percentIngredientList, name='percent-ingredient-list'),
    path('percent-ingredient-create/<int:id>', views.percentIngredientCreate, name='percent-ingredient-create'),
    path('percent-ingredient-delete/<int:id>',
         views.percentIngredientDelete, name='percent-ingredient-delete'),
    path('material-list', views.materialList, name='material-list'),
    path('material-create', views.materialCreate, name='material-create'),
    path('material-update/<int:id>', views.materialUpdate, name='material-update'),
    path('material-delete/<int:id>', views.materialDelete, name='material-delete'),
    path('percent-material-list', views.percentMaterialList, name='percent-material-list'),
    path('percent-material-create', views.percentMaterialCreate, name='percent-material-create'),
    path('labor-list', views.laborList, name='labor-list'),
    path('labor-create', views.laborCreate, name='labor-create'),
    path('labor-update/<int:id>', views.laborUpdate, name='labor-update'),
    path('labor-delete/<int:id>', views.laborDelete, name='labor-delete'),
    path('product-list', views.productList, name='product-list'),
    path('product-create', views.productCreate, name='product-create'),
    path('product-delete/<int:id>', views.productDelete, name='product-delete'),
    path('product/<int:id>',
         views.product, name='product'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile', views.profile, name='profile'),
]
