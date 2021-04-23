from django.apps import AppConfig


class TouristConfig(AppConfig):
    name = 'tourist'

    def ready(self):
        import tourist.signals
