from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from .models import Note, NoteShare, Profile

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

class NoteShareForm(forms.Form):

    uuid = forms.UUIDField(
        label="Recipient-User ID",
        error_messages={
            'invalid': "Enter a valid ID"
        },
        help_text='Ask the recipient for a secret User ID, which can be found in the "Secrets" tab.',
    )

    class Meta:
        pass

    def clean_uuid(self):
        data = super().clean()

        print(data)

        if len(self.errors) > 0:
            return data

        try:
            Profile.objects.get(id=data['uuid'])
        except Exception as e:
            raise ValidationError('No users with such ID')

        return data['uuid']
    