from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluye las rutas de la app "courses"
    path('', include('courses.urls')),
]
