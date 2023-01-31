from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'district'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ['district']
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ['district']
        })
    )


class Loiha41Admin(admin.ModelAdmin):
    list_display = ('district', 'time_update', 'time_create', 'is_published')
    list_display_links = ('district',)
    list_editable = ('is_published',)
    search_fields = ('district', 'time_create')

    fieldsets = (
        ('SANOAT', {
            'fields': ('bill_sum_industry', 'picture_of_growth_industry', 'forecast_industry', 'difference_industry')
        }),
        ('QISHLOQ', {
            'fields': ('bill_sum_locality', 'picture_of_growth_locality', 'forecast_locality', 'difference_locality')
        }),
        ('QURILISH', {
            'fields': ('bill_sum_construction', 'picture_of_growth_construction', 'forecast_construction', 'difference_construction')
        }),
        ('XIZMATLAR', {
            'fields': ('bill_sum_services', 'picture_of_growth_services', 'forecast_services', 'difference_services')
        }),
        ('CHAKANA SAVDO', {
            'fields': ('bill_sum_retail', 'picture_of_growth_retail', 'forecast_retail', 'difference_retail')
        }),
        ('TASHQI SAVDO AYLANMASI', {
            'fields': ('thousand_dollar_international_trade', 'picture_of_growth_international_trade')
        }),
        ('EKSPORT', {
            'fields': ('thousand_dollar_export', 'picture_of_growth_export')
        }),
        ('IMPORT', {
            'fields': ('thousand_dollar_import', 'picture_of_growth_import')
        }),
        ('IS_PUBLISHED', {
            'fields': ('is_published',)
        }),
        )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(District)
admin.site.register(Loiha41, Loiha41Admin)
admin.site.register(Loiha6)
admin.site.register(Loiha10)
admin.site.register(Loiha12)
admin.site.register(Loiha121)
admin.site.register(Loiha122)
admin.site.register(Loiha13)
admin.site.register(Loiha131)
admin.site.register(Loiha14)

