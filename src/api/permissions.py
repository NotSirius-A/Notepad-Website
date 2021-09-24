from rest_framework import permissions
from notepad.models import Profile


class IsNoteOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user)

        if profile is None:
            raise Exception('Request user does not have a profile')

        note = obj

        return (note.owner == profile)