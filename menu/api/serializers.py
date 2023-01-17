from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from recipe.models import Recipe, Tag, TagRecipe


#
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'title', 'slug', 'description')


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'author', 'title', 'text', 'image', 'tag', 'created', 'cooking_time')
        model = Recipe
        read_only_fields = ('author',)

    def get_author(self, obj):
        return obj.author.get_full_name()

# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True, slug_field='username'
#     )
#
#     class Meta:
#         fields = ('id', 'author', 'text', 'created', 'post')
#         model = Comment
#         read_only_fields = ('author', 'post')


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         slug_field='username',
#         read_only=True,
#         default=serializers.CurrentUserDefault()
#     )
#     following = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=User.objects.all()
#     )
#
#     class Meta:
#         fields = ('user', 'following')
#         model = Follow
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=Follow.objects.all(),
#                 fields=('user', 'following')
#             )
#         ]
#
#     def validate(self, data):
#         if data['following'] == self.context['request'].user:
#             raise serializers.ValidationError(
#                 'Нельзя подписаться на самого себя!')
#         return data
