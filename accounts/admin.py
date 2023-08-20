from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, UserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    # form = CustomUserChangeForm
    list_display = ('username','firstname','lastname','email', 'bio', 'image', 'is_active', 'is_superuser')
    list_filter = ('username', 'email', 'is_superuser', 'is_active')

    search_fields = ('email','username')
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {'fields' : ('username', 'firstname', 'lastname', 'email', 'bio', 'image', 'password')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('username', 'firstname', 'lastname', 'email', 'image', 'bio', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)