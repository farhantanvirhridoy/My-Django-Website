from django import forms
from django.forms import ModelForm
from .models import Venue, Event, Msg
    
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class MsgForm(ModelForm):
    class Meta:
        model = Msg
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
