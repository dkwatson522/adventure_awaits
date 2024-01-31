from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class ThemePark(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Guide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    parks = models.ManyToManyField(ThemePark)

class Booking(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    theme_park = models.ForeignKey(ThemePark, on_delete=models.CASCADE)
    date = models.DateField()

class Feedback(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
