# Import the path function from django.urls and the views module from this app
from django.urls import path

from . import views

# Set the app name for namespacing URLs
app_name = "core"

# Define the app's URL patterns
urlpatterns = [
    # Map the root URL to the index view
    path("", views.index, name="index"),
    # Map the /contact/ URL to the contact view
    path("contact/", views.contact, name="contact"),
    # Map the /signup/ URL to the signup view
    path("signup/", views.signup, name="signup"),
]