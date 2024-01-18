from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"article_slug": ["name"]}


class ArticleImageAdmin(admin.StackedInline):
    model = ArticleImage


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin]

    class Meta:
        model = Article


@admin.register(ArticleImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Slider)
admin.site.register(News)
admin.site.register(Anons)
admin.site.register(Events)
admin.site.register(Team)
admin.site.register(Map)
admin.site.register(Partners)


