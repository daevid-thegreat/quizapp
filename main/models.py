from django.db import models
import uuid

# Create your models here.
class Track(models.Model):
    trackname = models.CharField(max_length=264, unique=True)
    track_id = models.CharField(max_length=264, unique=True, default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.trackname

class Topic(models.Model):
    topic_id = models.CharField(max_length=264, unique=True, default=uuid.uuid4, primary_key=True)
    the_track = models.ForeignKey(Track, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    question_id = models.CharField(max_length=264, unique=True, default=uuid.uuid4, primary_key=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=264)
    answer = models.CharField(max_length=264)
    option1 = models.CharField(max_length=264)
    option2 = models.CharField(max_length=264)
    option3 = models.CharField(max_length=264)

    def __str__(self):
        return self.question

