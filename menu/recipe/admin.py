from django.contrib import admin

from .models import Recipe


# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'description', 'cooking_guide', 'image', 'created')
#     list_editable = ('group',)
#     search_fields = ('title',)
#     list_filter = ('created',)
#     empty_value_display = '-пусто-'


admin.site.register(Recipe)
