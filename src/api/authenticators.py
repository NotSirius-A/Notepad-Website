from django.contrib.auth import authenticate
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from notepad.models import Profile

class NoteAuthenticator(BaseAuthentication):
    def authenticate(self, request):
        # get usename and password from custom http headers, X-USERNAME and X-PASSWORD
        username = request.META.get('HTTP_X_USERNAME')
        password = request.META.get('HTTP_X_PASSWORD')

        if not username or not password:
            raise AuthenticationFailed('Provide full credentials, user X-USERNAME and X-PASSWORD custom http headers')

        user = authenticate(username=username, password=password)

        if user is None:
            raise AuthenticationFailed('No such user or invalid credentials')

        return (user, None)
