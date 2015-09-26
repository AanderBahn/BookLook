from django.contrib import admin

# Register your models here.
from .models import Reviewer#, ReviewerBooks


class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['name','email','timestamp','updated']
    class Meta:
      model = Reviewer

admin.site.register(Reviewer, ReviewerAdmin)

#admin.site.register(ReviewerBooks)
