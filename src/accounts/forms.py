from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm

from notepad.models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = AuthenticationForm.error_messages

    # overriding error message in a safe way,
    # error_messages.update({
    #     'invalid_login': 'dfsfs',
    # })


class CustomUserCreationForm(UserCreationForm):

    def save(self, *args, **kwargs):
        """
        Adding functionality on top of the save method:
        Automatically create a profile for the user
        """
        user = super().save()

        profile = Profile(user=user)
        profile.save()
