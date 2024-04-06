"""
Settings for the the Intra app.

Example:
    INTRA_RESET_PASSWORD_ENABLED (bool): Indicates whether the reset password
    feature is enabled in the Django project. Defaults to `False` if not
    specified in project settings.
"""

from django.conf import settings

INTRA_RESET_PASSWORD_ENABLED = getattr(
    settings, 'INTRA_RESET_PASSWORD_ENABLED', False
)

INTRA_ADMIN_LOGS_ENABLED = getattr(
    settings, 'INTRA_ADMIN_LOGS_ENABLED', False
)
