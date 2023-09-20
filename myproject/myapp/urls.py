from django.urls import path, include
from . import views


urlpatterns = [
    path('ingredient-list', views.ingredientList, name='ingredient-list'),
    path('ingredient-create', views.ingredientCreate,
         name='ingredient-create'),
    path('ingredient-update/<int:id>',
         views.ingredientUpdate, name='ingredient-update'),
    path('ingredient-delete/<int:id>',
         views.ingredientDelete, name='ingredient-delete'),
    path('material-list', views.materialList, name='material-list'),
    path('material-create', views.materialCreate, name='material-create'),
    path('material-update/<int:id>', views.materialUpdate, name='material-update'),
    path('material-delete/<int:id>', views.materialDelete, name='material-delete'),
    path('labor-list', views.laborList, name='labor-list'),
    path('labor-create', views.laborCreate, name='labor-create'),
    path('product-list', views.productList, name='product-list'),
    path('product-create', views.productCreate, name='product-create'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

]