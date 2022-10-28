from django.apps import AppConfig


class AppparadigmaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppParadigma'
    
    def ready(self):
        import AppParadigma.signals
