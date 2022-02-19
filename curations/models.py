from django.db import models
from django.contrib.auth import get_user, get_user_model


# Create your models here.
class Curation(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="curations"
    )
    subject = models.ForeignKey(
        "Subject", related_name="curations", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=64)
    curation = models.ForeignKey(Curation, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Link(models.Model):
    url = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.url} - {self.topic.title}"


class SubTopic(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.topic.title}"


class SubTopicLink(models.Model):
    url = models.URLField()
    subtopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtopic.title
