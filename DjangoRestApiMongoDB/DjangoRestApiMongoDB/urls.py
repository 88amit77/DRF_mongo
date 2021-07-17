from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials', include('tutorials.urls')),
    path('cards', include('cards.urls')),
 ]

