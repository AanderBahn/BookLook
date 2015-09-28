from django.contrib import admin

# Register your models here.
from .models import Book, Review


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','genre','isbn']
    class Meta:
      model = Book

admin.site.register(Book, BookAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','review','reviewer']
    class Meta:
      model = Review

admin.site.register(Review, BookAdmin)
