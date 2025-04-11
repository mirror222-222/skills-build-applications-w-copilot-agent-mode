from datetime import timedelta
from django.core.management.base import BaseCommand
from ...models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        self.stdout.write(f"Created user: {user1}")

        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')
        self.stdout.write(f"Created user: {user2}")

        # Add test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        self.stdout.write(f"Created team: {team1}")

        # Add test activities
        activity1 = Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        self.stdout.write(f"Created activity: {activity1}")

        activity2 = Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))
        self.stdout.write(f"Created activity: {activity2}")

        # Add test leaderboard entries
        leaderboard1 = Leaderboard.objects.create(user=user1, score=100)
        self.stdout.write(f"Created leaderboard entry: {leaderboard1}")

        leaderboard2 = Leaderboard.objects.create(user=user2, score=150)
        self.stdout.write(f"Created leaderboard entry: {leaderboard2}")

        # Add test workouts
        workout1 = Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        self.stdout.write(f"Created workout: {workout1}")

        workout2 = Workout.objects.create(name='HIIT', description='High-Intensity Interval Training for fat burning.')
        self.stdout.write(f"Created workout: {workout2}")

        # Add database query checks after each insertion
        self.stdout.write(f"Users in database: {list(User.objects.all())}")
        self.stdout.write(f"Teams in database: {list(Team.objects.all())}")
        self.stdout.write(f"Activities in database: {list(Activity.objects.all())}")
        self.stdout.write(f"Leaderboard entries in database: {list(Leaderboard.objects.all())}")
        self.stdout.write(f"Workouts in database: {list(Workout.objects.all())}")

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
