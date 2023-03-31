# Import necessary modules and classes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the project
urlpatterns = [
    # Include URLs defined in the 'core' app
    path("", include("core.urls")),
    # Include URLs defined in the 'item' app
    path("items/", include("item.urls")),
    # Include the built-in admin site
    path("dashboard/", include("dashboard.urls")),
    path("admin/", admin.site.urls),
    # Serve media files during development
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
