# booking/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import ThemePark, Guide, Booking, Feedback

class ThemeParkModelTest(TestCase):
    def setUp(self):
        ThemePark.objects.create(name="Disney World", location="Florida", description="A magical theme park.")

    def test_theme_park_creation(self):
        disney_world = ThemePark.objects.get(name="Disney World")
        self.assertEqual(disney_world.location, "Florida")

class GuideModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='guide1', password='12345')
        ThemePark.objects.create(name="Disney World", location="Florida", description="A magical theme park.")
        disney_world = ThemePark.objects.get(name="Disney World")
        Guide.objects.create(user=user, bio="Experienced guide.")
        guide = Guide.objects.get(user=user)
        guide.parks.add(disney_world)

    def test_guide_creation(self):
        user = User.objects.get(username='guide1')
        guide = Guide.objects.get(user=user)
        self.assertEqual(guide.bio, "Experienced guide.")
        self.assertIn(ThemePark.objects.get(name="Disney World"), guide.parks.all())

class GuideModelMethodsTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='guide1', password='12345')
        visitor = User.objects.create_user(username='visitor1', password='12345')
        ThemePark.objects.create(name="Disney World", location="Florida", description="A magical theme park.")
        disney_world = ThemePark.objects.get(name="Disney World")
        Guide.objects.create(user=user, bio="Experienced guide.")
        guide = Guide.objects.get(user=user)
        guide.parks.add(disney_world)

class BookingModelTest(TestCase):
    def setUp(self):
        visitor = User.objects.create_user(username='visitor1', password='12345')
        guide_user = User.objects.create_user(username='guide1', password='12345')
        guide = Guide.objects.create(user=guide_user, bio="Experienced guide.")
        theme_park = ThemePark.objects.create(name="Disney World", location="Florida", description="A magical theme park.")
        Booking.objects.create(guide=guide, visitor=visitor, theme_park=theme_park, date="2024-01-01")

    def test_booking_creation(self):
        booking = Booking.objects.get(visitor__username='visitor1')
        self.assertEqual(booking.guide.user.username, 'guide1')
        self.assertEqual(booking.theme_park.name, "Disney World")

class FeedbackModelTest(TestCase):
    def setUp(self):
        visitor = User.objects.create_user(username='visitor1', password='12345')
        guide_user = User.objects.create_user(username='guide1', password='12345')
        guide = Guide.objects.create(user=guide_user, bio="Experienced guide.")
        theme_park = ThemePark.objects.create(name="Disney World", location="Florida", description="A magical theme park.")
        booking = Booking.objects.create(guide=guide, visitor=visitor, theme_park=theme_park, date="2024-01-01")
        Feedback.objects.create(booking=booking, rating=5, comment="Excellent experience.")

    def test_feedback_creation(self):
        feedback = Feedback.objects.get(booking__visitor__username='visitor1')
        self.assertEqual(feedback.rating, 5)
        self.assertEqual(feedback.comment, "Excellent experience.")
