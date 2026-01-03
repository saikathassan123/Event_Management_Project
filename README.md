# Event Management System

A fully functional Django Event Management System with CRUD operations, optimized queries, and a responsive Tailwind CSS UI. Now configured with PostgreSQL database support.

## Features

- ✅ Complete CRUD operations for Events, Categories, and Participants
- ✅ Optimized database queries using `select_related` and `prefetch_related`
- ✅ Responsive UI with Tailwind CSS (via CDN)
- ✅ Organizer Dashboard with interactive statistics
- ✅ Search functionality for events by name or location
- ✅ Filter events by category and date range
- ✅ PostgreSQL database integration
- ✅ Environment variables using python-decouple
- ✅ Random data population command
- ✅ Django Debug Toolbar for query optimization

## Prerequisites

- Python 3.8+
- PostgreSQL (installed and running)
- pgAdmin 4 (optional, for database management)

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Setup

1. **Create Database in pgAdmin 4:**
   - Open pgAdmin 4
   - Connect to PostgreSQL server
   - Right-click "Databases" → Create → Database
   - Name: `Task_Management`
   - Click Save

2. **Create `.env` file** in project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DB_NAME=Task_Management
   DB_USER=postgres
   DB_PASSWORD=your-postgres-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Populate Random Data

```bash
# Default: 5 categories, 20 events, 30 participants
python manage.py populate_data

# Custom amounts
python manage.py populate_data --categories 10 --events 50 --participants 100
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Detailed Setup

See [SETUP.md](SETUP.md) for detailed installation instructions and troubleshooting.

## Project Structure

```
Assignment/
├── assignment/          # Django project settings
│   ├── settings.py     # PostgreSQL configuration
│   └── urls.py
├── events/             # Main application
│   ├── models.py       # Category, Event, Participant models
│   ├── views.py        # All CRUD views with optimized queries
│   ├── forms.py        # Model forms with Tailwind styling
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin registration
│   └── management/
│       └── commands/
│           └── populate_data.py  # Random data generator
├── templates/          # HTML templates
│   └── events/
├── .env               # Environment variables (create this)
├── requirements.txt   # Python dependencies
└── manage.py
```

## Key Features Implementation

### 1. Data Models (15 Marks)
- **Category**: name, description
- **Event**: name, description, date, time, location, category (ForeignKey)
- **Participant**: name, email, events (ManyToMany)

### 2. CRUD Operations (10 Marks)
- Full Create, Read, Update, Delete for all models
- Form validation included

### 3. Optimized Queries (10 Marks)
- `select_related('category')` for event list
- `prefetch_related('participants')` for events
- Aggregate query for total participants
- Filter by category and date range

### 4. UI with Tailwind CSS (35 Marks)
- Responsive design
- Navigation bar
- Organizer Dashboard with:
  - Stats grid (Total Events, Upcoming, Past, Total Participants)
  - Today's events listing
  - Interactive stats (clickable cards)

### 5. Search Features (10 Marks)
- Search by event name or location using `icontains`
- Filter by category
- Filter by date range

## Database Configuration

The project uses PostgreSQL by default. Configuration is managed through `.env` file:

```env
DB_NAME=Task_Management
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

To switch back to SQLite, comment out the PostgreSQL DATABASES config in `settings.py` and uncomment the SQLite configuration.

## Management Commands

### Populate Random Data

```bash
python manage.py populate_data [options]

Options:
  --categories N    Number of categories (default: 5)
  --events N        Number of events (default: 20)
  --participants N  Number of participants (default: 30)

Examples:
  python manage.py populate_data
  python manage.py populate_data --categories 10 --events 50 --participants 100
```

## Usage

1. **Create Categories**: Navigate to Categories → Add Category
2. **Create Events**: Navigate to Events → Add Event
3. **Add Participants**: Navigate to Participants → Add Participant
4. **View Dashboard**: Click Dashboard to see statistics and today's events
5. **Search Events**: Use the search bar on the Events page

## Environment Variables

All sensitive configuration is stored in `.env` file:
- `SECRET_KEY`: Django secret key
- `DB_NAME`: PostgreSQL database name
- `DB_USER`: PostgreSQL username
- `DB_PASSWORD`: PostgreSQL password
- `DB_HOST`: Database host (default: localhost)
- `DB_PORT`: Database port (default: 5432)

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Verify `.env` file has correct credentials
- Check database `Task_Management` exists in pgAdmin 4

### Module Not Found
```bash
pip install -r requirements.txt
```

### Migration Errors
```bash
python manage.py makemigrations
python manage.py migrate
```

## Notes

- Tailwind CSS is loaded via CDN (no build process required)
- Django Debug Toolbar is enabled for query optimization (if installed)
- All forms include proper validation
- The dashboard stats are interactive - click on Total Events, Upcoming Events, or Past Events to filter the list below

## License

This project is created for educational purposes.
