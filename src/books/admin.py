from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','genre','isbn']
    class Meta:
      model = Book

admin.site.register(Book, BookAdmin)
