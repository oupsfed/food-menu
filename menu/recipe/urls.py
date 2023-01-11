from django.urls import path

from . import views

app_name = 'recipe'


urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/create/', views.create_recipe, name='recipe_create'),
]
