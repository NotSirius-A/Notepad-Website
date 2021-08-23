from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page_view, name='login'),
    path('signup/', views.user_creation_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('secrets/', views.secrets_view, name='secrets'),
]