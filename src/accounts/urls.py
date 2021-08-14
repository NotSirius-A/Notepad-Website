from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page_view, name='login_page'),
    path('create/', views.user_creation_view, name='user_creation')
]