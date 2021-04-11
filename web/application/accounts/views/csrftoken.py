from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.generic import View


class CSRFToken(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(get_token(request))
