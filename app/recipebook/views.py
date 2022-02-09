from django.shortcuts import render
from django.views.generic import ListView, DetailView

from recipebook.models import Recipe, Ingredient


class RecipeIngredients:
    """Ингредиенты рецепта"""
    def get_ingredients(self):
        return Ingredient.objects.all()


class RecipeListView(RecipeIngredients, ListView):
    """Список рецептов"""
    model = Recipe
    queryset = Recipe.objects.filter(draft=False)


class RecipeDetailView(RecipeIngredients, DetailView):
    """Список рецептов"""
    model = Recipe
    slug_field = 'url'


class FilterRecipeView(RecipeIngredients, ListView):
    """Фильтр рецепов"""
    def get_queryset(self):
        return Recipe.objects.filter(ingredients__in=self.request.GET.getlist("ingr"))


class Search(RecipeIngredients, ListView):
    """Поиск по названию рецепта"""
    def get_queryset(self):
        return Recipe.objects.filter(title__icontains=self.request.GET.get("recipe_title"))
