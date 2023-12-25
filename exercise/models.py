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


# class SoccerSkill(models.Model):
#     """Specific skill that can be addressed by exercises."""
#
#     skill = models.CharField(max_length=50, choices=SoccerSkillTextChoices.choices)
#
#     def __str__(self):
#         return f"{self.skill}"


class AgeGroup(models.Model):
    """Specific age group that can be addressed by exercises."""

    AGE_GROUPS = (
        ("s", "Erwachsene"),
        ("a", "A-Jun"),
        ("b", "B-Jun"),
        ("c", "C-Jun"),
        ("d", "D-Jun"),
        ("e", "E-Jun"),
        ("f", "F-Jun"),
        ("g", "G-Jun"),
    )

    age_group = models.CharField(max_length=1, choices=AGE_GROUPS)

    def __str__(self):
        return f"{self.age_group}"


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

    # age_groups = models.ManyToManyField(AgeGroup, related_name="exercises")

    # def __str__(self):
    #     return f"{self.title}_{self.soccer_skills.get_skill_display()}"
