from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    name = 'Feedback'
    def ready(self):
        import Feedback.api.signals