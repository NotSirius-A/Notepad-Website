from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Note, NoteShare, Profile, User

@login_required(login_url='/login/')
def dashboard_view(request, *args, **kwargs):

    user_profile = Profile.objects.filter(user=request.user)[0]

    notes = Note.objects.filter(owner=user_profile)

    context = {
        'user_profile': user_profile,
        'notes': notes,
    }

    return render(request, 'notepad/dashboard.html', context)


@login_required(login_url='/login/')
def note_entire_view(request, *args, **kwargs):
    # uuid should be passed in the url like "..path/<uuid>/"
    UUID = kwargs['uuid']

    note = Note.objects.filter(id=UUID)[0]

    context = {
        'note': note
    }

    return render(request, 'notepad/note_entire.html', context)
