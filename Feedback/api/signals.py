from django.dispatch import receiver
from django.core.signals import request_finished,request_started
from django.db.models.signals import post_save
from Feedback.api.views import FeedbackCreate
from Feedback.models import Feedback
from Feedback import sentiment_analysis

@receiver(request_started)
def request_started(sender, **kwargs):
    print("Request Ended")
    kwargs['signal']['sender_receivers_cache']['test']='test value'
    print(sender)
@receiver(request_finished)
def request_finished(sender, **kwargs):
    print(kwargs['signal']['sender_receivers_cache']['test'])
    print(sender)

@receiver(post_save,sender=Feedback)
def create_feedback_sentiment(sender, **kwargs):
    # print(sender)
    feedback_object = kwargs['instance']
    sentiment_analysis.create_feedback_sentiment_object(feedback_object)