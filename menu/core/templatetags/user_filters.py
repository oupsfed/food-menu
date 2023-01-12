from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def count_author_things(things, author):
    return things.filter(author=author).count()
