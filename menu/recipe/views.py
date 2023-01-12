from dadata import Dadata
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .forms import RecipeForm
from .models import Recipe
from .utils import paginator

RECIPE_SHOW_LMT = 10


def index(request):
    recipe_list = Recipe.objects.all()
    page_obj = paginator(request, recipe_list, RECIPE_SHOW_LMT)
    context = {
        'recipe_list': recipe_list,
        'page_obj': page_obj,
    }
    return render(request, 'recipe/index.html', context)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe:index')
        return render(request, 'posts/create_recipe.html', {'form': form})
    form = RecipeForm()
    return render(request, 'recipe/create_recipe.html', {'form': form})
