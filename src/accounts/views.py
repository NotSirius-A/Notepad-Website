from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

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