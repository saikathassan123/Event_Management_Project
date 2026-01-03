# How to Deploy Event Management System to Live Server

## Why GitHub Doesn't Host Django Apps

GitHub is a **code repository** (storage), not a **web hosting service**. To make your Django app live, you need to deploy it to a hosting platform.

## Popular Free Hosting Options

### 1. **Render.com** (Recommended - Free Tier Available)
- Free PostgreSQL database
- Easy deployment from GitHub
- Automatic SSL certificates

### 2. **Railway.app** (Free Tier Available)
- Simple deployment
- Free PostgreSQL
- Good for beginners

### 3. **PythonAnywhere** (Free Tier Available)
- Python-focused hosting
- Easy setup
- Limited free tier

### 4. **Heroku** (Paid - No Free Tier Anymore)
- Professional hosting
- Requires credit card

## Step-by-Step: Deploy to Render.com (Free)

### Prerequisites
1. GitHub repository pushed (Event_Management_Project)
2. Render.com account (sign up at https://render.com)

### Step 1: Prepare Your Project

#### 1.1 Create `Procfile` (for Render)

Create a file named `Procfile` (no extension) in project root:

```
web: gunicorn assignment.wsgi:application
```

#### 1.2 Update `requirements.txt`

Make sure it includes production dependencies:

```
Django>=6.0
django-debug-toolbar>=6.0
python-decouple>=3.8
psycopg2-binary>=2.9.0
gunicorn>=21.2.0
whitenoise>=6.6.0
```

#### 1.3 Update `settings.py` for Production

Add these settings at the end of `assignment/settings.py`:

```python
# Production settings
import os

# Static files handling with WhiteNoise
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add WhiteNoise middleware (add this to MIDDLEWARE list)
# 'whitenoise.middleware.WhiteNoiseMiddleware',  # Add after SecurityMiddleware

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

#### 1.4 Create `runtime.txt` (Optional)

Create `runtime.txt` to specify Python version:

```
python-3.11.0
```

### Step 2: Deploy on Render

#### 2.1 Create New Web Service
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select repository: `Event_Management_Project`

#### 2.2 Configure Web Service
- **Name**: `event-management-system` (or any name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn assignment.wsgi:application`

#### 2.3 Create PostgreSQL Database
1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Name: `event-management-db`
3. Copy the **Internal Database URL**

#### 2.4 Add Environment Variables
In your Web Service settings, add these **Environment Variables**:

```
SECRET_KEY=your-secret-key-here (generate a new one)
DEBUG=False
DB_NAME=event_management_db (from PostgreSQL service)
DB_USER=your-db-user (from PostgreSQL service)
DB_PASSWORD=your-db-password (from PostgreSQL service)
DB_HOST=your-db-host.onrender.com (from PostgreSQL service)
DB_PORT=5432
ALLOWED_HOSTS=your-app-name.onrender.com
```

**OR use the Internal Database URL:**
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

#### 2.5 Deploy
1. Click **"Create Web Service"**
2. Render will build and deploy your app
3. Wait 5-10 minutes for deployment

### Step 3: Run Migrations

After deployment, run migrations:

1. Go to your Web Service in Render
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_data
```

### Step 4: Access Your Live Site

Your app will be available at:
```
https://your-app-name.onrender.com
```

## Alternative: Deploy to Railway.app

### Step 1: Sign up at Railway
1. Go to https://railway.app
2. Sign up with GitHub

### Step 2: Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose `Event_Management_Project`

### Step 3: Add PostgreSQL
1. Click **"+ New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway automatically sets `DATABASE_URL`

### Step 4: Configure Environment Variables
Add in Railway dashboard:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

### Step 5: Deploy
Railway auto-detects Django and deploys!

## Quick Setup Files Needed

I'll create the necessary files for you in the next step.

## Important Notes

1. **Never commit `.env` file** - Use environment variables in hosting platform
2. **Set `DEBUG=False`** in production
3. **Use production database** - Don't use SQLite in production
4. **Collect static files** - Run `python manage.py collectstatic`
5. **Set `ALLOWED_HOSTS`** - Add your domain

## Troubleshooting

### Static files not loading?
- Add `whitenoise` to middleware
- Run `collectstatic` command
- Check `STATIC_ROOT` setting

### Database connection error?
- Verify environment variables
- Check database is running
- Verify connection string

### 500 Internal Server Error?
- Check logs in hosting dashboard
- Verify `DEBUG=False` and check error logs
- Check `ALLOWED_HOSTS` setting

