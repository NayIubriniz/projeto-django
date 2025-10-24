from django.contrib import admin
from .models import Category, Recipe


class CategroryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategroryAdmin)
