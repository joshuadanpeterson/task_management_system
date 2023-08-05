# These lines of code are importing necessary modules and classes from Django's admin and auth modules.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# This class is used to manage the admin interface for Django's built-in User model.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        # You can include other fieldsets if you want to retain some sections.
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'is_active', 'is_staff')
    search_fields = ('username',)
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

