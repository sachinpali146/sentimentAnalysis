from rest_framework import serializers
from Feedback.models import Feedback, FeedbackSentiment


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('created', 'updated',)


class FeedbackSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackSentiment
        fields = '__all__'
        read_only_fields = ('created', 'updated',)
