from django.db import models

class Book(models.Model):
   title  = models.CharField(max_length=50)
   author = models.CharField(max_length=50)
   genre = models.CharField(max_length=50, default='?')
   isbn = models.CharField(max_length=50,null=True,blank=True)
   timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
   updated = models.DateTimeField(auto_now_add = False, auto_now=True)


   def __unicode__(self):
       return "%s" %(self.title)
