from django.conf.urls import url, include
from Feedback.api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^feedback/$', views.FeedbackCreate.as_view(), name='feedback_create'),
    url(r'^feedbackSentiment/list/$', views.FeedbackSentimentList.as_view(), name='feedback_sentiment_list'),
    url(r'^feedbackSentiment/(?P<pk>[0-9]+)/$', views.FeedbackSentimentDetail.as_view(),
        name='feedback_sentiment_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
