from django.contrib import admin

from exercise.models import AgeGroup
from exercise.models import Creator
from exercise.models import Exercise
from exercise.models import SoccerSkill

# Register your models here.

admin.site.register(SoccerSkill)
admin.site.register(Exercise)
admin.site.register(AgeGroup)
admin.site.register(Creator)
