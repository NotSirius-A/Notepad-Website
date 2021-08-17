from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Note, NoteShare, Profile

from .forms import NoteCreateEditForm

@login_required()
def dashboard_view(request, *args, **kwargs):
    try:
        user_profile = Profile.objects.filter(user=request.user)[0]
    except IndexError:
        raise Exception("Profile must be created alongside django-user, django-user without a profile tried to log in")

    notes = Note.objects.filter(owner=user_profile)

    context = {
        'user_profile': user_profile,
        'notes': notes,
    }

    return render(request, 'notepad/dashboard.html', context)


@login_required()
def note_entire_view(request, *args, **kwargs):
    # uuid should be passed in the url like "..path/<uuid>/"
    UUID = kwargs['uuid']

    user_profile = get_object_or_404(Profile, user=request.user)

    note = get_object_or_404(Note, id=UUID)
 
    is_authorized = False
    is_owner = False

    if user_profile == note.owner:
        is_authorized = True
        is_owner = True
    else:
        # find all note share objects for the requested note to later validate 
        # whether request.user is permitted to see it
        note_shares = NoteShare.objects.filter(note=note)

        for note_share in note_shares:
            if note_share.shared_to == user_profile:
                is_authorized = True

    # return 404 when unauthorized person tries to access the note
    if is_authorized != True:
        raise Http404
    

    context = {
        'note': note,
        'is_owner': is_owner,
        'user_profile': user_profile,
    }

    return render(request, 'notepad/note_entire.html', context)

@login_required
def note_create_view(request, *args, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)

    form = NoteCreateEditForm(data = request.POST or None)

    if form.is_valid():
        print(form.data)
    
        # automatically assign user as an owner
        note = form.save(commit=False)
        note.owner = user_profile
        note.save()

        return redirect('dashboard')

    context = {
        'form': form,
        'FRONTENDINFO_action': 'CREATE',
        'user_profile': user_profile,
    }
    return render(request, 'notepad/note_create_edit.html', context)

@login_required()
def note_edit_view(request, *args, **kwargs):
    # note uuid should be passed in the url like "..path/<uuid>/"
    UUID = kwargs['uuid']

    user_profile = get_object_or_404(Profile, user=request.user)

    note = get_object_or_404(Note, id=UUID)
 
    is_authorized = False
    is_owner = False

    if user_profile == note.owner:
        is_authorized = True
        is_owner = True

    # return 404 when unauthorized person tries to access the note
    if is_authorized != True or is_owner != True:
        raise Http404

    form = NoteCreateEditForm(instance=note, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("note_entire", args=[f"{UUID}"]))

    context = {
        'form': form,
        'FRONTENDINFO_action': 'EDIT',
        'user_profile': user_profile,
    }

    return render(request, 'notepad/note_create_edit.html', context)