from django.db import models
from django.contrib.auth.models import User


class HabitCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    category = models.ForeignKey(HabitCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    completed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('habit', 'date')

    def __str__(self):
        return f"{self.habit.name} - {self.date}"


class Reminder(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Reminder for {self.habit.name} at {self.time}"