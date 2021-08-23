from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import authenticate, login, logout

from notepad.models import Profile

from .forms import CustomAuthenticationForm, CustomUserCreationForm

# Create your views here.

def login_page_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = CustomAuthenticationForm(data=request.POST or None)

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if request.GET.get('next') is not None:
                return redirect(request.GET['next'])
            else:
                return redirect('homepage')

    context = {
        'form': form,
    }
    return render(request, 'accounts/login_page.html', context)

def user_creation_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = CustomUserCreationForm(data=request.POST or None)

    if form.is_valid():
        profile,user = form.save()
        login(request, user)
        return redirect('homepage')


    context = {
        'form': form,
    }

    return render(request, 'accounts/user_creation.html', context)


def logout_view(request, *args, **kwargs):
    logout(request)

    return redirect('homepage')

@login_required
def secrets_view(request, *args, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'accounts/user_secrets.html', context)