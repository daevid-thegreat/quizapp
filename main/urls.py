from . import views
from django.urls import path

urlpatterns = [
    path('tracks', views.track_list, name='track_list'),
    path('topics/<str:track_id>', views.topic_list, name='topic_list'),
    path('questions/<str:topic_id>', views.question_list, name='question_list'),
    path('options/<str:question_id>', views.question_options, name='question_options'),
    path('answer/<str:question_id>', views.question_answer, name='question_answer')
]