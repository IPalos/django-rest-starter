"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponsePermanentRedirect

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.middleware.security import SecurityMiddleware


class HTTPSRedirectMiddleware(SecurityMiddleware):
    def process_request(self, request):
        if not request.is_secure():
            # Redirect to HTTPS
            request_url = request.build_absolute_uri(request.get_full_path())
            secure_url = request_url.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(secure_url)
        return None

application = get_wsgi_application()
application = HTTPSRedirectMiddleware(application)
