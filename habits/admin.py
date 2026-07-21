from django.contrib import admin
from .models import HabitCategory, Habit, HabitLog, Reminder

admin.site.register(HabitCategory)
admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(Reminder)