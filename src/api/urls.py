from django.urls import path

from rest_framework import routers

from . import views


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'note', views.NoteViewSet)

urlpatterns = router.urls

# default django urlspatterns
#
# urlpatterns = [
#     path('note/<uuid:id>', views.NoteViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'partial_update', 'delete': 'destroy'}), name='note_retrieve'),
# ]
