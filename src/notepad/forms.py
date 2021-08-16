from django.forms import ModelForm

from .models import Note

class NoteEditForm(ModelForm):
    
    class Meta:
        model = Note
        fields = ('title', 'body')