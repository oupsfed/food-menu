from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from core.models import CreatedModel

User = get_user_model()


class Recipe(CreatedModel):
    title = models.CharField(
        'Название',
        max_length=200
    )
    text = RichTextField(
        'Текст рецепта',
        help_text='Введите описание рецепта',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipe'
    )
    # group = models.ForeignKey(
    #     Group,
    #     on_delete=models.SET_NULL,
    #     related_name='posts',
    #     blank=True,
    #     null=True,
    #     verbose_name='Группа',
    #     help_text='Группа, к которой будет относиться пост'
    # )
    image = models.ImageField(
        'Картинка',
        upload_to='recipe/',
        blank=True
    )
    cooking_time = models.IntegerField(
        'Время готовки'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title[:15]
