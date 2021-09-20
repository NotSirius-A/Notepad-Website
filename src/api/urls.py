from django.urls import path

from . import views

urlpatterns = [
    path('note/<uuid:id>', views.NoteViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'partial_update', 'delete': 'destroy'}), name='note_retrieve'),
]
