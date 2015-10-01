from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Group(models.Model):
    owner = models.ForeignKey(User, related_name="group_owner")
    likes = models.ManyToManyField(User, related_name="group_likes")
    name = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    semester = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User, related_name="question_likes")
    group = models.ForeignKey(Group)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, related_name="answer_author")
    likes = models.ManyToManyField(User, related_name="answer_likes")
    question = models.ForeignKey(Question)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
