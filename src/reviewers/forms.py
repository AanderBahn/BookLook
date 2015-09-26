from django import forms
from .models import Reviewer

class EmailForm(forms.Form):
  email = forms.EmailField(),
  name  = forms.CharField()

  #name = forms.CharField(max_length=300,null=True,blank=True)
  #email = forms.EmailField()

class ReviewerForm(forms.ModelForm):
  class Meta:
    model = Reviewer
    fields = ["name", "email"]

