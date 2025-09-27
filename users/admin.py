from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'phone_number', 'country')

    search_fields = ('email', 'phone_number')

    list_filter = ('is_staff', 'is_active', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('phone_number', 'country', 'avatar')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)