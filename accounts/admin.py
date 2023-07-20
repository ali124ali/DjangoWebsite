from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_superuser', 'is_active')

    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {'fields' : ('email', 'password')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)