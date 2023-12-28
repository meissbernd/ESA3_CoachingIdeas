from django.db import models
from django.urls import reverse

# Create your models here.


class Creator(models.Model):
    """Person that creates trainings content (e.g. exercises)."""

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class SoccerSkillTextChoices(models.TextChoices):
    """Enum of skills that can be addressed by exercises."""

    DRIBBLING = "Dribbling"
    PASSING = "Passen"
    FINISHING = "Torschuss"
    TRAPPING = "Ballannahme"
    COOPERATION = "Zusammenspiel"


class Exercise(models.Model):
    """Physical exercise for training."""

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
    soccer_skills = models.CharField(
        max_length=50, choices=SoccerSkillTextChoices.choices, null=True
    )
    for_adults = models.BooleanField(default=True)
    for_jun_a = models.BooleanField(default=False)
    for_jun_b = models.BooleanField(default=False)
    for_jun_c = models.BooleanField(default=False)
    for_jun_d = models.BooleanField(default=False)
    for_jun_e = models.BooleanField(default=False)
    for_jun_f = models.BooleanField(default=False)
    for_jun_g = models.BooleanField(default=False)
    image = models.ImageField(upload_to="exercise_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.title}_{self.soccer_skills.title()}"

    def get_absolute_url(self):
        return reverse("exercise_detail", args=[str(self.id)])
