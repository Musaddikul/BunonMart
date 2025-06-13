# accounts/middleware.py
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from django.utils.deprecation import MiddlewareMixin

class DynamicSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.site = Site.objects.get(domain=request.get_host().split(':')[0])
        except Site.DoesNotExist:
            request.site = RequestSite(request)  # fallback
