from django.apps import AppConfig


class MydjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mydjangoapp'
    def ready(self):
        from mydjangoapp.models import Task
