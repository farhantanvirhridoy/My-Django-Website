from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .models import Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from django.core.paginator import Paginator

def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Courier", 14)

    venues = Venue.objects.all()

    for venue in venues:
        textob.textLine(venue.name)
        textob.textLine(venue.address)
        textob.textOut(venue.zip_code)
        textob.textLine()
        textob.textLine("===================")

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venues.pdf')

def venue_csv(request):
    response = HttpResponse(content_type='csv/plain')
    response['Content-Disposition'] = "attachment; filename=venues.csv"

    venues = Venue.objects.all()
    writer = csv.writer(response)

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code])
    return response


def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = "attachment; filename=venues.txt"

    venues = Venue.objects.all()
    lines = []

    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n\n')

    response.writelines(lines)
    return response



def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('event_list')


def event_update_form(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None ,instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'event_update_form.html',{"form":form})






def add_event(request):
    submitted = False
    if (request.method=='POST'):
        form = EventForm(request.POST)
        form.save()
        submitted = True
    form = EventForm
    return render(request, 'add_event.html', {"form":form, "submitted":submitted})
    



def venue_update_form(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None ,instance=venue)
    if(request.method=="POST"):
        if form.is_valid():
            form.save()
            return redirect('list-venues')
    return render(request, 'venue_update_form.html',{"form":form})


def searching(request):
    key = request.POST['box']
    venues = Venue.objects.filter(name__contains=key)
    return render(request, 'searched_venue.html', {
        "key": key,
        "venues": venues
        })



def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html', {"venue": venue})



def list_venues(request):
    venues = Venue.objects.all()

    p = Paginator(venues, 3)
    page = request.GET.get('page')
    some_venues = p.get_page(page)
    return render(request, 'venue_list.html', {
        "venues": venues,
        "some_venues": some_venues,
        })


def add_venue(request):
    submitted = False
    if (request.method=='POST'):
        form = VenueForm(request.POST)
        form.save()
        submitted = True
    form = VenueForm
    return render(request, 'add_venue.html', {"form":form, "submitted":submitted})


def event_list(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, 'event_list.html', {
        "events" : events,
        })

# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Farhan"
    month = month.title()
    month_list = list(calendar.month_name)
    month_number = month_list.index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    time = now.strftime('%I:%M:%S %p')
    return render(request, 'home.html', {
        "name":name,
        "year": year,
        "month": month,
        "month_number":month_number,
        "month_list": month_list,
        "cal":cal,
        "time":time
        })