from django.shortcuts import redirect, render

def dashboard_view(request, *args, **kwargs):
    context = {

    }

    return render(request, 'notepad/dashboard.html', context)