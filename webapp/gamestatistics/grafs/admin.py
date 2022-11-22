from django.contrib import admin
from .models import Version, SubUser, Event

admin.site.register(Version)
admin.site.register(SubUser)
admin.site.register(Event)