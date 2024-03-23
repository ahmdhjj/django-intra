"""
URL configuration for the Intra app.
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import intra_settings

urlpatterns = []

if intra_settings.INTRA_RESET_PASSWORD_ENABLED:
    urlpatterns += [
        path(
            'password_reset/',
            auth_views.PasswordResetView.as_view(
                extra_context={'site_header': admin.site.site_header}
            ),
            name='admin_password_reset',
        ),
        path(
            'password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(
                extra_context={'site_header': admin.site.site_header}
            ),
            name='password_reset_done',
        ),
        path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                extra_context={'site_header': admin.site.site_header}
            ),
            name='password_reset_confirm',
        ),
        path(
            'reset/done/',
            auth_views.PasswordResetCompleteView.as_view(
                extra_context={'site_header': admin.site.site_header}
            ),
            name='password_reset_complete',
        ),
    ]

urlpatterns += [
    path('', admin.site.urls),
]
