from django import forms

from .models import Note

class NoteCreateEditForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ('title', 'body')
