from django.contrib import admin

from api.models import (
    Image,
    Icon,
    Task,
    List,
    Group,
)


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_per_page = 25



admin.site.register(Image, ImageAdmin)


class IconAdmin(admin.ModelAdmin):
    search_fields = ['new_icon', 'created_icon']
    list_per_page = 50


admin.site.register(Icon, IconAdmin)

admin.site.register(Task)


class ListAdmin(admin.ModelAdmin):
    list_display = ['icon','title']
    search_fields = ['title']
    list_per_page = 45
    ordering = ['title']
    pass

admin.site.register(List)
admin.site.register(Group)