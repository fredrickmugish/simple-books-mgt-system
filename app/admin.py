from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'price']
    list_display = ['title', 'price']


# Register your models here.
admin.site.register(Book, BookAdmin)
