from reviewers.models import Reviewer

class ReferMiddleware():
  def process_request(self, request):
      name = request.GET.get("name")
      try:
          obj = Reviewer.objects.get(name = name)
      except:
          obj = None

      if obj:
         request.session['reviewer_name_ref'] = obj
