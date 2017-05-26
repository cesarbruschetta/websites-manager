from django.contrib import admin
from .models import FilePathModel, LinksModel


@admin.register(FilePathModel)
class FilePathAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    search_fields = ('title',)

    # Group user info
    fieldsets = (
        ('Principal', {'fields': ('title', 'path_root', 'path_url', 'slug',)}),
    )


@admin.register(LinksModel)
class LinksAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    search_fields = ('title',)
