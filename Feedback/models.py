from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField

# Create your models here.
MIN_VALUE = 1
MAX_VALUE = 10


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    review = models.TextField(null=True, blank=True)
    timely_response = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE), MaxValueValidator(MAX_VALUE)])
    support_experience = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE), MaxValueValidator(MAX_VALUE)])
    overall_experience = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE), MaxValueValidator(MAX_VALUE)])
    overall_satisfaction = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE), MaxValueValidator(MAX_VALUE)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class FeedbackSentiment(models.Model):
    feedback = models.ForeignKey(Feedback)
    review_analysis = models.TextField(null=True, blank=True)
    review_best_lines = models.TextField(null=True, blank=True)
    review_worst_lines = models.TextField(null=True, blank=True)
    review_best_sentiment = models.FloatField(null=True, blank=True)
    review_worst_sentiment = models.FloatField(null=True, blank=True)
    review_overall_sentiment = models.FloatField(null=True, blank=True)
    input_sentiment = models.FloatField()
    overall_sentiment = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
