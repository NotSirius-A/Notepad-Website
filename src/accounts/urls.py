from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page_view, name='login_page'),
    path('signup/', views.user_creation_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]