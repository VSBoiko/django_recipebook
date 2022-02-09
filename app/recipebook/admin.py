from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Recipe, RecipeImages, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Рецепты"""
    list_display = ("title", "get_image", "url", "draft")
    list_filter = ("ingredients", "draft")
    search_fields = ("title", "recipe__name")
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["published", "unpublished"]
    readonly_fields = ("get_image",)
    fieldsets = (
        ("Рецепт", {
            "fields": ("title", "description", "instruction")
        }),
        ("Главное фото", {
            "fields": ("poster", "get_image")
        }),
        ("Ингредиенты", {
            "fields": ("ingredients",)
        }),
        ("Опции", {
            "fields": ("url", "draft")
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src="{ obj.poster.url }" width="100" height="110">')

    def published(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    def unpublished(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    get_image.short_description = "Постер"

    published.short_description = "Опубликовать"
    published.allowed_permissions = ("change",)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ("change",)


@admin.register(RecipeImages)
class RecipeImagesAdmin(admin.ModelAdmin):
    """Фото для рецепта"""
    list_display = ("title", "recipe", "get_image")
    search_fields = ("recipe__title",)
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={ obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Ingredient)

admin.site.site_title = "Django Recipe Book"
admin.site.site_header = "Django Recipe Book"
