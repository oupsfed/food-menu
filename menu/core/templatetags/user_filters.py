from django import template

from recipe.models import Recipe, Tag

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def count_author_things(things, author):
    return things.filter(author=author).count()


@register.filter
def count_tags(tag):
    return Recipe.objects.filter(tag=tag).count()


@register.filter
def show_recipe_tags(recipe):
    return Tag.objects.filter(recipe=recipe).all()
