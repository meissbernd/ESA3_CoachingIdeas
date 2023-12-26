from django.db import models


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
    age_adults = models.BooleanField(default=True)
    age_jun_a = models.BooleanField(default=False)
    age_jun_b = models.BooleanField(default=False)
    age_jun_c = models.BooleanField(default=False)
    age_jun_d = models.BooleanField(default=False)
    age_jun_e = models.BooleanField(default=False)
    age_jun_f = models.BooleanField(default=False)
    age_jun_g = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.title}_{self.soccer_skills.get_skill_display()}"
