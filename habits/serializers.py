from rest_framework import serializers
from .models import HabitCategory, Habit, HabitLog, Reminder


class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name']


class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'date', 'completed']


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'habit', 'time', 'active']


class HabitSerializer(serializers.ModelSerializer):
    logs = HabitLogSerializer(many=True, read_only=True)
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Habit
        fields = ['id', 'owner', 'name', 'description', 'frequency', 'category', 'created_at', 'logs', 'reminders']
        read_only_fields = ['owner']