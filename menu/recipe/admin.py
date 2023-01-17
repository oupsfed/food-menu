from django.contrib import admin

from .models import Recipe, Tag, TagRecipe

# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'description', 'cooking_guide', 'image', 'created')
#     list_editable = ('group',)
#     search_fields = ('title',)
#     list_filter = ('created',)
#     empty_value_display = '-пусто-'


admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(TagRecipe)
