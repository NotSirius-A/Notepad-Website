from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page_view, name='login_page'),
]