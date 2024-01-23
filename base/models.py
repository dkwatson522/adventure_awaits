from django.db import models
from django.contrib.auth.models import User

class Guide(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    parks = models.ManyToManyField('Park', related_name='parks', null=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Rating(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars'),
        ]
    )
    feedback = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback[0:50]

class Park(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    guides = models.ManyToManyField(Guide, related_name='guides', null=True)

class GuideParkRelationship(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, null=True)
