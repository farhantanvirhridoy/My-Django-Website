from django.db import models


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
