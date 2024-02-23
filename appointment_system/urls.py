from django.urls import path
from appointment_system.views import hello_world  # Import your view

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
