from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelSmokeTests(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'test@example.com')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups', description='Pushups workout')
        self.assertEqual(str(workout), 'Pushups')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        workout = Workout.objects.create(name='Pushups', description='Pushups workout')
        activity = Activity.objects.create(user=user, workout=workout, date='2024-01-01', duration=30)
        self.assertEqual(str(activity), 'test@example.com - Pushups')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100')
