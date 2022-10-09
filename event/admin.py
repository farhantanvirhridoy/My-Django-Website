from django.contrib import admin
from .models import Venue
from .models import Myuser
from .models import Event

admin.site.register(Venue)
admin.site.register(Myuser)
admin.site.register(Event)
# Register your models here.
