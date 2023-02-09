import random
from . import serializers
from .models import Topic, Quiz, Track
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# get every track
@api_view(['GET'])
def track_list(request):
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 12
    try:
        tracks = Track.objects.all()
        result_page = paginator.paginate_queryset(tracks, request)
        serializer = serializers.TrackSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Track.DoesNotExist:
        return Response(status=404)

# get topics in a track
@api_view(['GET'])
def topic_list(request, track_id):
    try:
        topics = Topic.objects.filter(track=track_id)
        serializer = serializers.TopicSerializer(topics, many=True)
        paginator = pagination.PageNumberPagination()
        paginator.page_size = 12
        return Response(serializer.data)
    except Topic.DoesNotExist:
        return Response(status=404)

# get questions in a topic
@api_view(['GET'])
def question_list(request, topic_id):
    try:
        questions = Quiz.objects.filter(topic=topic_id)
        serializer = serializers.QuizSerializer(questions, many=True)
        paginator = pagination.PageNumberPagination()
        paginator.page_size = 12
        return Response(serializer.data)
    except Quiz.DoesNotExist:
        return Response(status=404)

# get a question options
@api_view(['GET'])
def question_options(request, question_id):
    try:
        question = Quiz.objects.get(id=question_id)
        # randomlize the options
        options = [question.answer, question.option1, question.option2, question.option3]
        random.shuffle(options)
        serializer = serializers.QuestionSerializer(question)
        return Response({'options': options})
    except Quiz.DoesNotExist:
        return Response(status=404)

# get a question answer
@api_view(['GET'])
def question_answer(request, question_id):
    try:
        question = Quiz.objects.get(id=question_id)
        serializer = serializers.QuizSerializer(question)
        return Response(serializer.data.get('answer'))
    except Quiz.DoesNotExist:
        return Response(status=404)