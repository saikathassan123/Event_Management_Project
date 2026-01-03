# Quick Start Guide - Event Management System

## Step-by-Step Setup

### Step 1: Create .env File

Copy `env_template.txt` to `.env` and update the database password:

```bash
# In project root (E:\Django\Assignment)
copy env_template.txt .env
```

Then edit `.env` and replace `your-postgres-password-here` with your actual PostgreSQL password.

### Step 2: Install Dependencies

```bash
# Activate virtual environment
.\task_env\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 3: Create Database in pgAdmin 4

1. Open pgAdmin 4
2. Connect to PostgreSQL server
3. Right-click "Databases" → Create → Database
4. Name: `Task_Management`
5. Click Save

### Step 4: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Populate Random Data

```bash
python manage.py populate_data
```

This creates:
- 5 Categories
- 20 Events
- 30 Participants

### Step 6: Start Server

```bash
python manage.py runserver
```

Open browser: http://127.0.0.1:8000/

## Custom Data Population

```bash
# More data
python manage.py populate_data --categories 10 --events 50 --participants 100

# Less data
python manage.py populate_data --categories 3 --events 10 --participants 15
```

## Troubleshooting

**Database Connection Error?**
- Check PostgreSQL is running
- Verify `.env` file has correct password
- Ensure database `Task_Management` exists

**Module Not Found?**
```bash
pip install -r requirements.txt
```

**Migration Errors?**
```bash
python manage.py makemigrations
python manage.py migrate
```

## What's Next?

- Visit Dashboard: http://127.0.0.1:8000/
- View Events: http://127.0.0.1:8000/events/
- Admin Panel: http://127.0.0.1:8000/admin/

Enjoy your Event Management System! 🎉

