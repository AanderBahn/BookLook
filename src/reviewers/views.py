from django.shortcuts import render, HttpResponseRedirect
#from.django.contrib import messages

from.forms  import  ReviewerForm, EmailForm
from.models import Reviewer

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

def myPage(request, name):
  #print name
  context = {"name": name}
  template = "myPage.html"
  return render(request, template, context)


def home(request):
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
    if created:
      new_reviewer_old.ref_name = get_ref_name()
      # add our books that we reffer to out reviewer profile or related
      if not obj == None:
        new_reviewer_old.book = obj
      new_reviewer_old.ip_address = get_ip(request)
      new_reviewer_old.save()

    #print all "books" that read as a result of being reviewed

    #redirect here
    return HttpResponseRedirect("/%s" %(new_reviewer_old.name))


  context = {"form": form}
  template = "home.html"
  return render(request, template, context)
