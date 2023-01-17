from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Recipe


class RecipeForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Recipe
        fields = ('title',
                  'text',
                  'cooking_time',
                  'tag',
                  'image',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if not data:
            raise forms.ValidationError('Пост не можеть быть без текста!')
        return data