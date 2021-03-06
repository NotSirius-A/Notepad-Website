from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.user.username)

    def get_shortusername(self):
        MAX_LENGTH = 25
        username = str(self.user)

        if len(username) > MAX_LENGTH:
            username = username[:MAX_LENGTH] + "..."

        return username
            


class Note(models.Model):
    MAX_NOTE_LENGTH = int(1e+4)
    MAX_TITLE_LENGTH = 100

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    body = models.CharField(max_length=MAX_NOTE_LENGTH)

    title = models.CharField(max_length=MAX_TITLE_LENGTH)

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    # models.ImageField

    class Meta:
        ordering = ['-date_edited']

    def __str__(self):
        return f"{self.title}: {self.owner}"

    def get_short_title(self):
        MAX_LENGTH = 45
        title = self.title

        if len(title) > MAX_LENGTH:
            title = title[:MAX_LENGTH] + "..."
        
        return title

class NoteShare(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_to = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return None
