from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from.forms  import  BookForm
from.models import Book

def myPage(request):
 template = "inLook.html"
 return render(request, template, context)

#context = {"form": form}
template = "home.html"
#return render(request, template, context)
