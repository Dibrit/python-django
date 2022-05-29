from django.contrib import admin
from account.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'country')
    list_filter = ('automatic_box', 'company')
    fieldsets = (
        ('optional', {
            'fields': ('automatic_box', 'insurance_date', 'name', 'asd')
        }),
        ('obligatory', {
            'fields': ('color', 'company', 'year', 'country', 'owner', 'is_damaged')
        }),
    )
