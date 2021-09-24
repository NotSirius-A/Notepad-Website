from rest_framework import serializers
from notepad.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title','body', 'date_created', 'date_edited']
    