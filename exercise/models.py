from django.contrib.auth.models import User
from django.db import models


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
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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

    image = models.ImageField(upload_to="exercise/images/", null=True, blank=True)

    pdf = models.FileField(upload_to="exercise/pdfs/", blank=True)

    youtube_link = models.URLField(blank=True, null=True)

    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(0, 6)])

    def __str__(self):
        return f"{self.title}_{self.soccer_skills.title()}"

    def delete(self, *args, **kwargs):
        """Delete the files in media-folder when exercise is deleted."""
        self.pdf.delete()
        self.image.delete()
        super().delete(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(0, 6)])

    def __str__(self):
        return self.text
