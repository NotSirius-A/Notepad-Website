from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('view/<uuid:uuid>', views.note_entire_view, name='note_entire'),
]