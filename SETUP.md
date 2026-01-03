# Event Management System - Setup Guide

## Prerequisites

1. Python 3.8+
2. PostgreSQL (installed and running)
3. pgAdmin 4 (for database management)

## Installation Steps

### 1. Create Virtual Environment (if not already created)

```bash
python -m venv task_env
.\task_env\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup in pgAdmin 4

1. Open pgAdmin 4
2. Connect to your PostgreSQL server
3. Right-click on "Databases" → "Create" → "Database"
4. Database name: `Task_Management`
5. Click "Save"

### 4. Create .env File

Create a `.env` file in the project root directory (`E:\Django\Assignment\.env`) with the following content:

```env
# Django Settings
SECRET_KEY=django-insecure-&5qgin)4692r9c6@l)-((kkmi44b!s*w#%hcz)7d2ayu_g9q2p

# Database Configuration (PostgreSQL)
DB_NAME=Task_Management
DB_USER=postgres
DB_PASSWORD=your-postgres-password-here
DB_HOST=localhost
DB_PORT=5432

# Optional: Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Important:** Replace `your-postgres-password-here` with your actual PostgreSQL password.

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Populate Database with Random Data

```bash
# Default: 5 categories, 20 events, 30 participants
python manage.py populate_data

# Custom amounts
python manage.py populate_data --categories 10 --events 50 --participants 100
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Troubleshooting

### Database Connection Error

If you get a database connection error:

1. Make sure PostgreSQL is running
2. Check your `.env` file has correct credentials
3. Verify database `Task_Management` exists in pgAdmin 4
4. Check PostgreSQL is listening on port 5432

### Module Not Found Error

If you get `ModuleNotFoundError`:

```bash
# Make sure virtual environment is activated
.\task_env\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Migration Errors

If migrations fail:

```bash
# Delete migration files (except __init__.py) in events/migrations/
# Then recreate migrations
python manage.py makemigrations
python manage.py migrate
```

## Project Structure

```
Assignment/
├── assignment/          # Django project settings
│   ├── settings.py      # Updated with PostgreSQL config
│   └── urls.py
├── events/              # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── management/
│   │   └── commands/
│   │       └── populate_data.py  # Command to populate random data
│   └── ...
├── templates/           # HTML templates
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
└── manage.py
```

## Features

- ✅ PostgreSQL database connection
- ✅ Environment variables using python-decouple
- ✅ Random data population command
- ✅ Full CRUD operations
- ✅ Optimized queries
- ✅ Responsive Tailwind CSS UI
- ✅ Search and filter functionality

