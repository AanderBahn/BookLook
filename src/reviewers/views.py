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

def myPage(request):
  print name
  context = {"name": name}
  template = "myPage.html"
  return render(request, template, context)


def home(request):
  #print request.META.get("REMOTE_ADDR")
  #print request.META.get("HTTP_X_FORWARDED_FOR")
  #print request.POST["email"], print request.POST["email_2"],

  #This is using Reg Django Forms
  #form = EmailForm(request.POST or None)
  #if form.is_valid():
  #  email= form.cleaned_data['email']
  #  new_reviewer, created = Reviewer.objects.get_or_create(email=email)
  #  print new_reviewer, created
  #  print new_reviewer.timestamp
  #  if created:
  #   print "This Obj was created"

  #model form
  form = ReviewerForm(request.POST or None) #Reviewer
  if form.is_valid():
    new_reviewer = form.save(commit=False)
    #might do something here
    email= form.cleaned_data['email']
    name= form.cleaned_data['name']
    new_reviewer_old, created = Reviewer.objects.get_or_create(email=email)
    if created:
      #new_reviewer_old.ref_id = get_ref_id()
      new_reviewer_old.ip_address = get_ip(request)
      #new_reviewer_old.name = get_name()
      new_reviewer_old.save()
      #messages.success(request, 'Profile created.')
      #success_message = "Profile was created successfully"
    #redirect here
    return HttpResponseRedirect("/%s" %(new_reviewer_old.name))
    #new_reviewer.ip_address = get_ip(request)
    #new_reviewer.save()

  context = {"form": form}
  template = "home.html"
  return render(request, template, context)
