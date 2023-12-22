from django.db import models


# Create your models here.


class Creator(models.Model):
    """Person that creates trainings content (e.g. exercises)."""

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class SoccerSkill(models.Model):
    """Specific skill that can be addressed by exercises."""

    label = models.CharField(max_length=30)


class AgeGroup(models.Model):
    """Specific age group that can be addressed by exercises."""

    label = models.CharField(max_length=30)


class Exercise(models.Model):
    """Physical exercise for training."""

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
    soccer_skills = models.ManyToManyField(SoccerSkill, related_name="exercises")
    age_groups = models.ManyToManyField(AgeGroup, related_name="exercises")
