from rest_framework.routers import DefaultRouter
from .views import HabitCategoryViewSet, HabitViewSet, HabitLogViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'categories', HabitCategoryViewSet)
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'logs', HabitLogViewSet, basename='habitlog')
router.register(r'reminders', ReminderViewSet, basename='reminder')

urlpatterns = router.urls