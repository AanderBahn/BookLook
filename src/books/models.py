from django.db import models
from reviewers.models import Reviewer

class Book(models.Model):
   title  = models.CharField(max_length=50)
   author = models.CharField(max_length=50)
   genre = models.CharField(max_length=50, blank=True)
   isbn = models.CharField(max_length=50,null=True,blank=True)
   timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
   updated = models.DateTimeField(auto_now_add = False, auto_now=True)


   def __unicode__(self):
       return "%s" %(self.title)

class Review(models.Model):
  title = models.ForeignKey(Book)
  reviewer = models.ForeignKey(Reviewer,unique=True)
  review = models.TextField(max_length=500)

  def __unicode__(self):
       return "%s" %(self.title)
