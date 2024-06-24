from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('admin_profile', views.admin_profile, name='admin_profile'),
]