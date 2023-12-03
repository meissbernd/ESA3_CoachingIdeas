from django.db import models


# Create your models here.


class Creator(models.Model):
    """Person that creates trainings content (e.g. exercises)."""

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Exercise(models.Model):
    """Physical exercise for training."""

    description = models.CharField(max_length=40)
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
