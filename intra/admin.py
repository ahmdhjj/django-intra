"""
Admin configuration for LogEntry model.
"""
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from intra.intra_settings import INTRA_ADMIN_LOGS_ENABLED


class LogEntryAdmin(admin.ModelAdmin):
    """
    Admin options for LogEntry model.
    """
    list_display = [
        '__str__',
        'user',
        'content_type',
        'change_message',
    ]

    list_filter = [
        ('user', admin.RelatedOnlyFieldListFilter),
        'content_type',
        'action_flag',
    ]

    def has_add_permission(self, request):
        """
        Disable adding LogEntry objects via the admin interface.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Disable changing LogEntry objects via the admin interface.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Disable deleting LogEntry objects via the admin interface.
        """
        return False


if INTRA_ADMIN_LOGS_ENABLED:
    admin.site.register(LogEntry, LogEntryAdmin)
