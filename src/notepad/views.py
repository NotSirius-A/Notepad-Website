from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dashboard_view(request, *args, **kwargs):
    context = {

    }

    return render(request, 'notepad/dashboard.html', context)