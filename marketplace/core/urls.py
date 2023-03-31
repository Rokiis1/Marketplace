# Import the path function from django.urls and the views module from this app
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

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
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]