from django.contrib import admin

from myapp.models import TextImage


# Register your models here.
class TextImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ['title']


admin.site.register(TextImage, TextImageAdmin)
