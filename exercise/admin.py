from django.contrib import admin

from exercise.models import Creator
from exercise.models import Exercise


# Register your models here.

# admin.site.register(SoccerSkillTextChoices)
admin.site.register(Exercise)
admin.site.register(Creator)
