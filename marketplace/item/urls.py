# Import the `path` function from the `django.urls` module.
# Also import the `views` module from the current directory (`.`).
from django.urls import path

from . import views

# Set the namespace for these URLs to `item`.
app_name = 'item'

# Define the urlpatterns for this app.
# This URL pattern matches a path with an integer parameter `pk`.
# The path calls the `detail` view function from `views.py`.
# The URL pattern name is `detail`, which can be used to reverse the URL.
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]
