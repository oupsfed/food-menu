from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title',
                  'description',
                  'cooking_guide',
                  'cooking_time',
                  'image',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if not data:
            raise forms.ValidationError('Пост не можеть быть без текста!')
        return data