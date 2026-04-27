from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Pref


@admin.register(Pref)
class PrefAdmin(admin.ModelAdmin):
    # Admin configuration for the Pref model (Japanese prefectures).
    # Displays prefecture names in the admin list view and allows searching by name.
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Admin configuration for the CustomUser model, extending Django's UserAdmin.
    # Adds custom fields (tel, pref) to the admin form and list views, and enables filtering by pref.
    fieldsets = UserAdmin.fieldsets + (
        ('Additional fields', {'fields': ('tel', 'pref')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active', 'pref', 'tel')
    list_filter = ('is_staff', 'is_active', 'pref')
