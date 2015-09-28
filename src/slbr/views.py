from django.shortcuts import render


def testHome(request):
  context = {}
  template = "elseWise.html"
  return render(request, template, context)

#def book(request):
 # context = {}
  #template = "book.html"
  #return render(request, template, context)
