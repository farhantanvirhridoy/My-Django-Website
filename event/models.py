from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

from django.core.exceptions import ObjectDoesNotExist
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
    


class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Myuser(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name  = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank = True)
    attendees = models.ManyToManyField(Myuser)

    def __str__(self):
        return self.name

class Msg(models.Model):
    name  = models.CharField(max_length=120)
    msg = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ': ' + self.msg
# Create your models here.
