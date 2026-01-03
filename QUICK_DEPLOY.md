# Quick Deployment Guide - Event Management System

## Why GitHub Doesn't Host Your App

**GitHub = Code Storage** (like a folder in the cloud)  
**Hosting Platform = Live Server** (where your app actually runs)

You need BOTH:
1. ✅ GitHub - to store your code
2. ✅ Hosting Platform - to run your app live

## Fastest Way: Deploy to Render.com (FREE)

### Step 1: Push Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/Event_Management_Project.git
git push -u origin main
```

### Step 2: Sign Up on Render

1. Go to https://render.com
2. Sign up with GitHub (free)

### Step 3: Create PostgreSQL Database

1. Click **"New +"** → **"PostgreSQL"**
2. Name: `event-management-db`
3. Copy the **Internal Database URL** (you'll need this)

### Step 4: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect GitHub → Select `Event_Management_Project`
3. Configure:
   - **Name**: `event-management-system`
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   - **Start Command**: 
     ```
     gunicorn assignment.wsgi:application
     ```

### Step 5: Add Environment Variables

In Web Service → Environment, add:

```
SECRET_KEY=generate-a-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=paste-your-internal-database-url-here
```

**To generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 6: Deploy

Click **"Create Web Service"** and wait 5-10 minutes.

### Step 7: Run Migrations

1. Go to your Web Service
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_data
```

### Step 8: Your Live URL

Your app will be at:
```
https://your-app-name.onrender.com
```

## Alternative: Railway.app (Even Easier)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select `Event_Management_Project`
5. Add **PostgreSQL** database
6. Add environment variables:
   - `SECRET_KEY=your-secret-key`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=*.railway.app`
7. Railway auto-deploys!

## Files Already Created for You

✅ `Procfile` - Tells hosting platform how to run your app  
✅ `runtime.txt` - Specifies Python version  
✅ `requirements.txt` - Updated with production dependencies  
✅ `settings.py` - Updated for production deployment  

## Important Notes

1. **Never commit `.env`** - Use environment variables in hosting platform
2. **Set `DEBUG=False`** in production
3. **Your app URL** will be provided by the hosting platform
4. **Database** will be automatically created by hosting platform

## Troubleshooting

**Static files not loading?**
- Already fixed with WhiteNoise in settings.py

**Database error?**
- Check `DATABASE_URL` environment variable is set correctly

**500 Error?**
- Check logs in hosting dashboard
- Verify all environment variables are set

## Need Help?

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

