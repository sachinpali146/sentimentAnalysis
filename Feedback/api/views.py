from django.shortcuts import render
from Feedback.models import Feedback, FeedbackSentiment
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from Feedback.api.serializers import FeedbackSerializer, FeedbackSentimentSerializer


# Create your views here.

class FeedbackCreate(generics.CreateAPIView):
    serializer_class = FeedbackSerializer


class FeedbackSentimentList(generics.ListAPIView):
    serializer_class = FeedbackSentimentSerializer
    queryset = FeedbackSentiment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class FeedbackSentimentDetail(generics.RetrieveAPIView):
    serializer_class = FeedbackSentimentSerializer
    queryset = FeedbackSentiment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
