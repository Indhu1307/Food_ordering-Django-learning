from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('menu.urls')),  # Include the menu app URLs
    path('', include('menu.urls')), # home page
]
