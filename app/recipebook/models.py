from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    """Ингредиенты"""
    name = models.CharField("Название", max_length=300, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    """Рецепт"""
    title = models.CharField("Название", max_length=300)
    description = models.TextField("Описание")
    instruction = models.TextField("Инструкция приготовления")
    poster = models.ImageField("Главное фото", upload_to="recipe_posters/")
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ингрединеты")
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeImages(models.Model):
    """Фото для рецепта"""
    title = models.CharField("Название", max_length=300)
    image = models.ImageField("Фото", upload_to="recipe_images/")
    recipe = models.ForeignKey(
        Recipe, verbose_name="Рецепт", on_delete=models.CASCADE, related_name="recipe_images"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография для рецепта"
        verbose_name_plural = "Фотографии для рецепта"
