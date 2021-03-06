# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 12:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField(blank=True, null=True)),
                ('timely_response', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('support_experience', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('overall_experience', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('overall_satisfaction', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_analysis', models.TextField(blank=True, null=True)),
                ('review_best_lines', models.TextField(blank=True, null=True)),
                ('review_worst_lines', models.TextField(blank=True, null=True)),
                ('review_best_sentiment', models.FloatField(blank=True, null=True)),
                ('review_worst_sentiment', models.FloatField(blank=True, null=True)),
                ('review_overall_sentiment', models.FloatField(blank=True, null=True)),
                ('input_sentiment', models.FloatField()),
                ('overall_sentiment', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Feedback')),
            ],
        ),
    ]
