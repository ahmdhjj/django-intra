"""
URL configuration for the tests.
"""

from django.urls import path, include


urlpatterns = [
    path('admin/', include('intra.urls')),
]
