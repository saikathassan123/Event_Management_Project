"""
Management command to populate the database with random data for Events, Categories, and Participants.
Usage: python manage.py populate_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Category, Event, Participant
from datetime import timedelta, time
import random

class Command(BaseCommand):
    help = 'Populates the database with random sample data for Events, Categories, and Participants'

    def add_arguments(self, parser):
        parser.add_argument(
            '--categories',
            type=int,
            default=5,
            help='Number of categories to create (default: 5)'
        )
        parser.add_argument(
            '--events',
            type=int,
            default=20,
            help='Number of events to create (default: 20)'
        )
        parser.add_argument(
            '--participants',
            type=int,
            default=30,
            help='Number of participants to create (default: 30)'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data population...'))
        
        num_categories = options['categories']
        num_events = options['events']
        num_participants = options['participants']

        # Clear existing data (optional - comment out if you want to keep existing data)
        # self.stdout.write(self.style.WARNING('Clearing existing data...'))
        # Participant.objects.all().delete()
        # Event.objects.all().delete()
        # Category.objects.all().delete()

        # Create Categories
        self.stdout.write(self.style.SUCCESS(f'Creating {num_categories} categories...'))
        category_names = [
            'Technology', 'Business', 'Education', 'Entertainment', 'Sports',
            'Health & Wellness', 'Arts & Culture', 'Science', 'Food & Drink', 'Travel',
            'Music', 'Fashion', 'Photography', 'Gaming', 'Networking'
        ]
        category_descriptions = [
            'Tech conferences, workshops, and seminars',
            'Business meetings, networking events, and conferences',
            'Educational workshops, courses, and seminars',
            'Entertainment shows, concerts, and performances',
            'Sports events, tournaments, and competitions',
            'Health workshops, yoga sessions, and wellness programs',
            'Art exhibitions, cultural festivals, and performances',
            'Science fairs, research presentations, and lectures',
            'Food festivals, cooking classes, and tastings',
            'Travel meetups, adventure trips, and tours',
            'Music concerts, festivals, and live performances',
            'Fashion shows, style workshops, and exhibitions',
            'Photography workshops, exhibitions, and contests',
            'Gaming tournaments, esports events, and conventions',
            'Networking events, meetups, and social gatherings'
        ]

        categories = []
        for i in range(num_categories):
            name = category_names[i % len(category_names)]
            # Add number if category already exists
            if Category.objects.filter(name=name).exists():
                name = f"{name} {i+1}"
            category = Category.objects.create(
                name=name,
                description=category_descriptions[i % len(category_descriptions)]
            )
            categories.append(category)
            self.stdout.write(f'  Created category: {category.name}')

        # Create Participants
        self.stdout.write(self.style.SUCCESS(f'Creating {num_participants} participants...'))
        first_names = [
            'John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'James', 'Emma',
            'Robert', 'Olivia', 'William', 'Sophia', 'Richard', 'Isabella', 'Joseph',
            'Ava', 'Thomas', 'Mia', 'Charles', 'Charlotte', 'Daniel', 'Amelia',
            'Matthew', 'Harper', 'Anthony', 'Evelyn', 'Mark', 'Abigail', 'Donald',
            'Elizabeth', 'Steven', 'Sofia', 'Paul', 'Aria', 'Andrew', 'Scarlett'
        ]
        last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
            'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Wilson',
            'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee',
            'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis',
            'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott',
            'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams'
        ]

        participants = []
        for i in range(num_participants):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            name = f"{first_name} {last_name}"
            email = f"{first_name.lower()}.{last_name.lower()}{i}@example.com"
            
            participant = Participant.objects.create(
                name=name,
                email=email
            )
            participants.append(participant)
            if (i + 1) % 10 == 0:
                self.stdout.write(f'  Created {i + 1} participants...')

        # Create Events
        self.stdout.write(self.style.SUCCESS(f'Creating {num_events} events...'))
        event_names = [
            'Annual Tech Summit', 'Business Networking Night', 'Python Workshop',
            'Jazz Music Festival', 'Marathon Run', 'Yoga Retreat', 'Art Exhibition',
            'Science Fair', 'Food Festival', 'Travel Expo', 'Rock Concert',
            'Fashion Week', 'Photography Contest', 'Gaming Tournament',
            'Startup Pitch Night', 'Data Science Conference', 'Web Development Bootcamp',
            'Design Thinking Workshop', 'AI & Machine Learning Summit', 'Blockchain Forum',
            'Digital Marketing Masterclass', 'Leadership Seminar', 'Innovation Hub',
            'Creative Writing Workshop', 'Film Festival', 'Comedy Night',
            'Dance Performance', 'Theater Show', 'Poetry Reading', 'Book Launch'
        ]
        locations = [
            'Convention Center', 'Grand Hotel', 'City Hall', 'University Campus',
            'Sports Complex', 'Art Gallery', 'Concert Hall', 'Community Center',
            'Tech Hub', 'Business District', 'Park Amphitheater', 'Museum',
            'Stadium', 'Conference Room A', 'Auditorium', 'Exhibition Hall',
            'Outdoor Venue', 'Rooftop Terrace', 'Beach Resort', 'Mountain Lodge'
        ]
        cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

        today = timezone.now().date()
        
        for i in range(num_events):
            # Random date between 30 days ago and 60 days in the future
            days_offset = random.randint(-30, 60)
            event_date = today + timedelta(days=days_offset)
            
            # Random time
            hour = random.randint(9, 20)
            minute = random.choice([0, 15, 30, 45])
            event_time = time(hour, minute)
            
            event_name = random.choice(event_names)
            if i > 0 and random.random() < 0.3:  # 30% chance to add year/month
                event_name = f"{event_name} {event_date.year}"
            
            location = f"{random.choice(locations)}, {random.choice(cities)}"
            
            description = f"Join us for an exciting {event_name.lower()}. This event brings together professionals, enthusiasts, and experts in the field. Don't miss out on this amazing opportunity to learn, network, and have fun!"
            
            event = Event.objects.create(
                name=event_name,
                description=description,
                date=event_date,
                time=event_time,
                location=location,
                category=random.choice(categories)
            )
            
            # Assign random participants to events (2-8 participants per event)
            num_participants_for_event = random.randint(2, min(8, len(participants)))
            event_participants = random.sample(participants, num_participants_for_event)
            event.participants.set(event_participants)
            
            if (i + 1) % 5 == 0:
                self.stdout.write(f'  Created {i + 1} events...')

        self.stdout.write(self.style.SUCCESS('\nData population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Summary:'))
        self.stdout.write(self.style.SUCCESS(f'   - Categories: {Category.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   - Events: {Event.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   - Participants: {Participant.objects.count()}'))

