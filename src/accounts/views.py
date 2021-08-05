from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from . import forms

# Create your views here.

def login_page_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = forms.CustomAuthenticationForm(data=request.POST or None)

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
