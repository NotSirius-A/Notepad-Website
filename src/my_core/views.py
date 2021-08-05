from django.shortcuts import render, redirect
from django.urls import reverse

def homepage_view(request, *args, **kwargs):
    user = request.user

    context = {
        'user': user, 
    }

    # redirect user to a dashboard page instead of homepage
    if user.is_authenticated:
        return redirect(reverse('dashboard', current_app='notepad'))

    return render(request, 'my_core/homepage.html', context)
