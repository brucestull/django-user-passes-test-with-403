from django.apps import AppConfig


class ForbiddenAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forbidden_app'
