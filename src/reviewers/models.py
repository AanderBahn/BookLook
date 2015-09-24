from django.db import models

# Create your models here.

class Reviewer(models.Model):
   name  = models.CharField(max_length=300,null=True,blank=True)
   email = models.EmailField()
   #ref_id = models.CharField(max_length=120, default='ABC')
   ip_address = models.CharField(max_length=120, default='ABC')
   timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
   updated = models.DateTimeField(auto_now_add = False, auto_now=True)


   def __unicode__(self):
       return "%s" %(self.email)

class Meta:
  unique_together = ("email", "name") #"ref_id",