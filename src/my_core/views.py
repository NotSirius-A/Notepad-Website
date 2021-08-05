from django.shortcuts import render, redirect


def homepage_view(request, *args, **kwargs):
    context = {

    }

    return render(request, 'my_core/homepage.html', context)