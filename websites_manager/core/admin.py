from django.contrib import admin
from .models import FilePathModel

# Register your models here.


@admin.register(FilePathModel)
class FilePathAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    search_fields = ('title',)

    # Group user info
    fieldsets = (
        ('Principal', {'fields': ('title', 'path_root', 'path_url', 'slug',)}),
    )
