# Import necessary modules
import random
import string
from django.utils import timezone
from django.contrib.auth.models import User
from base.models import ThemePark, Guide, GuideRating, Booking

# Function to generate a random string
def random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Define functions to seed data
def seed_data():
    # Create theme parks
    disney_world = ThemePark.objects.create(name="Disney World", location="Orlando, Florida")
    disneyland = ThemePark.objects.create(name="Disneyland", location="Anaheim, California")
    universal_studios = ThemePark.objects.create(name="Universal Studios", location="Los Angeles, California")

    # Create users
    for i in range(10):  # Create 10 users as an example
        username = f'user{i+1}_{random_string()}'  # Append a random string to the base username
        email = f'user{i+1}@example.com'
        password = 'password123'  # You may want to change this
        User.objects.create_user(username=username, email=email, password=password)

    # Create guides
    for user in User.objects.all():
        guide = Guide.objects.create(user=user, bio="Sample bio")
        # Add expertise (just an example, modify as needed)
        if user.username.startswith("user1"):
            guide.expertise.add(disney_world)
        elif user.username.startswith("user2"):
            guide.expertise.add(disneyland)
        else:
            guide.expertise.add(universal_studios)

    # Create guide ratings
    guides = Guide.objects.all()
    for guide in guides:
        GuideRating.objects.create(guide=guide, rating=random.randint(1, 5))

    # Create bookings
    for _ in range(10):  # Create 10 bookings as an example
        guide = random.choice(guides)
        theme_park = random.choice([disney_world, disneyland, universal_studios])
        user = random.choice(User.objects.all())  # Randomly select a user for each booking
        date = timezone.now() + timezone.timedelta(days=random.randint(1, 30))
        Booking.objects.create(guide=guide, theme_park=theme_park, user=user, date=date)

# Call the seed_data function
seed_data()
