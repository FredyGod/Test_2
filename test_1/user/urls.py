from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create, name='create'),
    path('profile/<int:pk>/delete', Delete.as_view(), name='delete'),
]
