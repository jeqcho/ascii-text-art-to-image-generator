from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ascii-to-image/', include('ascii_to_image.urls')),
    path('admin/', admin.site.urls),
]