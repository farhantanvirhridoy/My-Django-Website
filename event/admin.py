from django.contrib import admin
from .models import Venue
from .models import Myuser
from .models import Event, Msg

admin.site.register(Venue)
admin.site.register(Myuser)
admin.site.register(Event)
admin.site.register(Msg)
# Register your models here.
