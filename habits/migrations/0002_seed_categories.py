from django.db import migrations


def seed_categories(apps, schema_editor):
    HabitCategory = apps.get_model('habits', 'HabitCategory')
    categories = [
        'Work and Career',
        'Self Care',
        'Financial',
        'Household',
        'Productivity',
        'Mental Health',
        'Physical Health',
        'Relationship and Family',
        'Personal Development',
        'Creative',
    ]
    for name in categories:
        HabitCategory.objects.get_or_create(name=name)


def remove_categories(apps, schema_editor):
    HabitCategory = apps.get_model('habits', 'HabitCategory')
    HabitCategory.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_categories, remove_categories),
    ]