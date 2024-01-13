from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'gender')
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('name', 'surname', 'birth_date', 'avatar', 'gender')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'surname', 'birth_date', 'avatar', 'gender')}),
    )


admin.site.register(User, CustomUserAdmin)
