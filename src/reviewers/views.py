from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms  import  ReviewerForm, EmailForm
from .models import Reviewer

from books.forms import BookForm, ReviewForm
from books.models import Book, Review

def get_ip(request):
  try:
      x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
      if x_forward:
        ip = x_forward.split(",")[0]
      else:
        ip = request.META.get("REMOTE_ADDR")
  except:
        ip = ""
  #pass
  return ip

def get_ref_name():
  return 'book'

#str(user_id)[:11].replace('-', '')
import uuid

#def get_ref_id():
#  #ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
#  #ref_id = '########'
#  try:
#    id_exists = Reviewer.objects.get(ref_id=ref_id)
#    print "run getting the id"
#    #get_ref_id()
#  except:
#    return ref_id

#def get_name():
#  name = str()
#  return name

def newReview(request):
  form = ReviewForm(request.POST or None)
  if form.is_valid():
    new_Review = form.save(commit=False)
    title = form.cleaned_data['title']
    review = form.cleaned_data['review']
    reviewer = form.cleaned_data['reviewer']
    new_review_old, created = Review.objects.get_or_create(title=title, review=review, reviewer=reviewer)
    template = "myPage.html"
    context = {"form": form}
    return render(request, template, context)

  template = "newReview.html"
  context = {"form": form}
  return render(request, template, context)


def newBook(request):
  form = BookForm(request.POST or None)
  if form.is_valid():
    new_book = form.save(commit=False)
    title = form.cleaned_data['title']
    author = form.cleaned_data['author']
    genre = form.cleaned_data['genre']
    isbn = form.cleaned_data['isbn']
    new_book_old, created = Book.objects.get_or_create(title=title, author=author, genre=genre, isbn=isbn)
    template = "myPage.html"
    context = {"form": form}
    return render(request, template, context)

  template = "newBook.html"
  context = {"form": form}
  return render(request, template, context)

def myPage(request, name):
 books_review = Review.objects.all()
 #review = books_review.objects.get(all)


 template = "myPage.html"
 context = {"books_review": books_review}
 return render(request, template, context)


def home(request):
  #username = request.POST['username']
  #password = request.POST['password']
  #user = authenticate(username=username, password=password)
  try:
    reviewer_name = request.session['reviewer_name_ref']
    obj = Reviewer.objects.get(name=reviewer_name)
  except:
      obj = None

  form = ReviewerForm(request.POST or None)
  if form.is_valid():
    new_reviewer = form.save(commit=False)
    email = form.cleaned_data['email']
    name = form.cleaned_data['name']
    new_reviewer_old, created = Reviewer.objects.get_or_create(email=email, name=name)

    #redirect here
    return HttpResponseRedirect("/%s" %(new_reviewer_old.name))


  context = {"form": form}
  template = "home.html"
  return render(request, template, context)
