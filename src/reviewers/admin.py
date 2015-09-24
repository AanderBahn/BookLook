from django.contrib import admin

# Register your models here.
from .models import Reviewer


class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['email','name','timestamp','updated']
    class Meta:
      model = Reviewer

admin.site.register(Reviewer, ReviewerAdmin)
