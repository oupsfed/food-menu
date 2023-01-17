from dadata import Dadata
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe, Tag, TagRecipe
from .utils import paginator

RECIPE_SHOW_LMT = 10


def index(request):
    recipe_list = Recipe.objects.all()
    tag_list = Tag.objects.all()
    recipe_tag_list = TagRecipe.objects.all()
    page_obj = paginator(request, recipe_list, RECIPE_SHOW_LMT)
    context = {
        'recipe_list': recipe_list,
        'tag_list': tag_list,
        'recipe_tag_list': recipe_tag_list,
        'page_obj': page_obj,
    }
    return render(request, 'recipe/api_index.html', context)


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


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    # comments = post.comments.all()
    # form = CommentForm()
    context = {
        'recipe': recipe,
        # 'comments': comments,
        # 'form': form
    }
    return render(request, 'recipe/recipe_detail.html', context)
