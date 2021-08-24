from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('view/<uuid:uuid>', views.note_entire_view, name='note_entire'),
    path('edit/<uuid:uuid>', views.note_edit_view, name='note_edit'),
    path('create/', views.note_create_view, name='note_create'),
    path('delete/<uuid:uuid>', views.note_delete_view, name='note_delete'),
    path('share/<uuid:uuid>', views.note_share_view, name='note_share'),
]