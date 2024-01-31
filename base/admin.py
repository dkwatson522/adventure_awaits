from django.contrib import admin
from .models import Booking, Guide, ThemePark, Feedback

admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Guide)
admin.site.register(ThemePark)
