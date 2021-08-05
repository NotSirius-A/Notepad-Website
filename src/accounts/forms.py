from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = AuthenticationForm.error_messages

    # overriding error message in a safe way,
    # error_messages.update({
    #     'invalid_login': 'dfsfs',
    # })
