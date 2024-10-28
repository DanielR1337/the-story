from django.urls import path
from .import views

app_name = 'core'  # This defines the namespace

urlpatterns = [
    path("", views.retrieve_bird_api, name="retrieve-bird-api"),
]