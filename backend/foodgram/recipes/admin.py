from django.contrib import admin
from django.db.models import Count, OuterRef
from recipes.models import Favorite, Ingredient, Recipe, Tag


class TagsInline(admin.TabularInline):
    model = Recipe.tags.through
    extra = 3


class IngredientsInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'favorite_count',
    )
    inlines = (
        TagsInline,
        IngredientsInline
    )
    fields = ('name', 'author', 'image', 'text', 'cooking_time',
              'favorite_count')
    readonly_fields = ('favorite_count', )
    list_filter = ('author', 'name', 'tags')

    def get_queryset(self, request):
        return Recipe.objects.annotate(
            favorite_count=Count(
                Favorite.objects.filter(recipe=OuterRef('pk')).values('id')
            )
        )

    @admin.display(
        ordering='favorite_count',
        description='Количество добавлений в избранное',
    )
    def favorite_count(self, obj):
        return obj.favorite_count


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug'
    )
    ordering = ('-name', )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit'
    )
    list_filter = ('name', )
