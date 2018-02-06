import argparse
import json
import sys, os
from django.conf import settings
import googleapiclient.discovery
from .models import FeedbackSentiment
from collections import defaultdict

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

TIMELY_RESPONSE_WEIGHT = .2
SUPPORT_EXPERIENCE_WEIGHT = .2
OVERALL_EXPERIENCE_WEIGHT = .25
OVERALL_SATISFACTION_WEIGHT = .35
INPUT_SENTIMENT_WEIGHT = .35
REVIEW_SENTIMENT_WEIGHT = .65


def get_native_encoding_type():
    """Returns the encoding type that matches Python's native strings."""
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'


def analyze_sentiment(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeSentiment(body=body)
    sentiment_response = None
    while sentiment_response is None:
        try:
            sentiment_response = request.execute()
        except OSError:
            sentiment_response = None
    response = dict()
    response['review_analysis'] = json.dumps(sentiment_response)
    response['review_overall_sentiment'] = sentiment_response['documentSentiment']['score']
    sentences = defaultdict(list)
    for sentence in sentiment_response['sentences']:
        sentences[sentence['sentiment']['score']].append(sentence['text']['content'])
    response['review_worst_sentiment'] = min(sentences.keys())
    response['review_worst_lines'] = '.\n'.join(sentences[min(sentences.keys())])
    response['review_best_sentiment'] = max(sentences.keys())
    response['review_best_lines'] = '.\n'.join(sentences[max(sentences.keys())])
    return response


def analyze_input_sentiment(feedback):
    mapping_dict = {
        1: -1,
        2: -.8,
        3: -.5,
        4: -.2,
        5: 0,
        6: .2,
        7: .4,
        8: .6,
        9: .8,
        10: 1,
    }
    final_value = (mapping_dict[feedback.timely_response] * TIMELY_RESPONSE_WEIGHT) + (
            mapping_dict[feedback.support_experience] * SUPPORT_EXPERIENCE_WEIGHT) + (
                          mapping_dict[feedback.overall_experience] * OVERALL_EXPERIENCE_WEIGHT) + (
                          mapping_dict[feedback.overall_satisfaction] * OVERALL_SATISFACTION_WEIGHT)
    return final_value


def create_feedback_sentiment_object(feedback):
    feedback_sentiment = FeedbackSentiment()
    feedback_sentiment.feedback = feedback
    feedback_sentiment.input_sentiment = analyze_input_sentiment(feedback)
    feedback_sentiment.overall_sentiment = feedback_sentiment.input_sentiment
    if feedback.review:
        feedback_analysis = analyze_sentiment(feedback.review, get_native_encoding_type())
        feedback_sentiment.review_analysis = feedback_analysis['review_analysis']
        feedback_sentiment.review_best_lines = feedback_analysis['review_best_lines']
        feedback_sentiment.review_worst_lines = feedback_analysis['review_worst_lines']
        feedback_sentiment.review_best_sentiment = feedback_analysis['review_best_sentiment']
        feedback_sentiment.review_worst_sentiment = feedback_analysis['review_worst_sentiment']
        feedback_sentiment.review_overall_sentiment = feedback_analysis['review_overall_sentiment']
        feedback_sentiment.overall_sentiment = (feedback_analysis[
                                                    'review_overall_sentiment'] * REVIEW_SENTIMENT_WEIGHT) + (
                                                       feedback_sentiment.input_sentiment * INPUT_SENTIMENT_WEIGHT)
    feedback_sentiment.save()
