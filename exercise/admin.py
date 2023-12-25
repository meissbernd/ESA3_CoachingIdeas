from django.contrib import admin

from exercise.models import AgeGroup
from exercise.models import Creator
from exercise.models import Exercise

# from exercise.models import SoccerSkillTextChoices

# Register your models here.

# admin.site.register(SoccerSkillTextChoices)
admin.site.register(Exercise)
admin.site.register(AgeGroup)
admin.site.register(Creator)
