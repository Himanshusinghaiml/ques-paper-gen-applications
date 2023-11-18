from django.db import models

# Create your models here.
# question_generator/models.py
from django.db import models

class QuestionStore(models.Model):
    question = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    marks = models.IntegerField()

    def __str__(self):
        return self.question