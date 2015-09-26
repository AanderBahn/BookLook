from django import forms
from .models import Book

class BookForm(forms.Form):
  title  = forms.CharField(),
  author = forms.CharField(),
  genre  = forms.CharField(),
  isbn   = forms.CharField()



class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ["title", "author","genre","isbn"]

