from django.db import models

# Create your models here.

class Reviewer(models.Model):
   name  = models.CharField(max_length=300,null=True,blank=True)
   email = models.EmailField()
   ref_name = models.CharField(max_length=120, default='ABC')
   ip_address = models.CharField(max_length=120, default='ABC')
   timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
   updated = models.DateTimeField(auto_now_add = False, auto_now=True)


   def __unicode__(self):
       return "%s" %(self.email)

class Meta:
  unique_together = ("email", "name") #"ref_id",

#class ReviewerBooks(models.Model):
#  name = models.OneToOneField(Reviewer, related_name="Reviewed")
#  booked = models.ManyToManyField(Reviewer, related_name="booked", null=True, blank=True)
#  nameall = models.ForeignKey(Reviewer, related_name='nameall')

#  def __unicode__(self):
#      print "booked are ", self.booked.all()
#      print self.nameall
#      print self.name
#      return self.booked.all()[0].name
