from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from .models import HabitCategory, Habit, HabitLog, Reminder
from .serializers import (
    HabitCategorySerializer,
    HabitSerializer,
    HabitLogSerializer,
    ReminderSerializer,
    RegisterSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class HabitCategoryViewSet(viewsets.ModelViewSet):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitLogViewSet(viewsets.ModelViewSet):
    serializer_class = HabitLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HabitLog.objects.filter(habit__owner=self.request.user)


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(habit__owner=self.request.user)