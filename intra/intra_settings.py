from django.conf import settings

INTRA_RESET_PASSWORD_ENABLED = getattr(
    settings, 'INTRA_RESET_PASSWORD_ENABLED', False
)
