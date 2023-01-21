from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate

# IMPORT do not use "app_settings.py strategy" as that is not compatible with @override_settings (unittests)
# this strategy is
APP_SETTINGS = dict(
    MAIL_FROM=None,
    SLACK_APP_TOKEN=None,
    SLACK_TEAM=None,
)


class NotificationsConfig(AppConfig):
    name = 'notifications'
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        for k, v in APP_SETTINGS.items():
            _k = 'NOTIFICATIONS_%s' % k
            if not hasattr(settings, _k):
                setattr(settings, _k, v)

        post_migrate.connect(create_events, sender=self)


def create_events(sender, **kwargs):
    from .models import EventRef, Event

    for ref in EventRef.get_references():
        Event.objects.update_or_create(name=ref.name, defaults={'description': ref.description})
