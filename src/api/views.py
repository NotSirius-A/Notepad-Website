from notepad.models import Note, Profile


from .authenticators import NoteAuthenticator
from .serializers import NoteSerializer
from .permissions import IsNoteOwner

from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication

class NoteViewSet(viewsets.ModelViewSet):
    """
    Note managment API
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, NoteAuthenticator]
    permission_classes = [IsNoteOwner]

    def perform_create(self, serializer):
        # this method needs to be overriden,
        # normally it just saved data from serializer to a model instance, 
        # but its required to inject the note owner profile which is derived from the sessionid
        
        profile = Profile.objects.get(user=self.request.user)

        if profile is None:
            raise Exception("Request user does not have a profile associated with them")

        Note.objects.create(**serializer.data, owner=profile)

