from django.urls import path

from . import views

app_name = 'recipe'


urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/create/', views.create_recipe, name='recipe_create'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
