# HabitLoop Backend

Django REST Framework backend for HabitLoop, a habit tracking app with streaks, categories, and reminders.

## Tech Stack
- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- API Docs: drf-spectacular (Swagger/OpenAPI)
- Docker + Docker Compose
- Deployed on Railway

## Features
- User registration & JWT login
- Habit CRUD (create, edit, delete)
- Habit categories
- Daily/weekly habit logging with streak tracking
- Reminders per habit
- Fully documented REST API

## API Documentation
Live Swagger docs: `/api/docs/`

## Local Setup

```bash
git clone https://github.com/adisacodes/habitloop-backend.git
cd habitloop-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or run the full stack with Docker:

```bash
docker compose up --build
```

## Live Deployment
Backend: https://habitloop-backend-production.up.railway.app

## Related Repo
Frontend: https://github.com/adisacodes/habitloop-frontend

## ER Diagram
See [docs/er-diagram.md](docs/er-diagram.md)