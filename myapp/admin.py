from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myapp.models import TextImage, User


# Register your models here.
class TextImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ['title']


class CustomVendorAdmin(UserAdmin):
    model = User
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'created_at',
        'updated_at')
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number')
    list_filter = ('gender', 'created_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'gender',
                'place_of_birth', 'datetime_of_birth', 'address', 'city',
                'country_of_origin',
            )
        }),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'user_permissions')}),
        ('Group Permissions', {'fields': ('groups', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(TextImage, TextImageAdmin)
admin.site.register(User, CustomVendorAdmin)
