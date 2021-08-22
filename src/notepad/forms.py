from django import forms
from django.contrib.auth.decorators import login_required

from .models import Note

class NoteCreateEditForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ('title', 'body')

        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'note-title',
            'placeholder': 'Title'}
            ),
        'body': forms.Textarea(attrs={
            'class': 'note-body',
            'placeholder': 'Write your note here'}
            )
        }

        labels = {
            'title': '',
            'body': '',
        }

