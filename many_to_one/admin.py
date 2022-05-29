from django.contrib import admin
from many_to_one.models import Reporter, Article


class BooksInstanceInline(admin.TabularInline):
    model = Article


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', )
    inlines = [BooksInstanceInline, ]
