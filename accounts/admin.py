from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Pref


@admin.register(Pref)
class PrefAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional fields', {'fields': ('tel', 'pref')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active', 'pref', 'tel')
    list_filter = ('is_staff', 'is_active', 'pref')
