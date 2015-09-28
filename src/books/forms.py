from django import forms
from .models import Book, Review

class BookForm(forms.Form):
  title  = forms.CharField(),
  author = forms.CharField(),
  genre  = forms.CharField(),
  isbn   = forms.CharField()



class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ["title", "author","genre","isbn"]

class ReviewForm(forms.Form):
  title = forms.ModelChoiceField(queryset=Book.objects.all().order_by('title'))
  reviewer = forms.CharField()

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ["title","review","reviewer"]
