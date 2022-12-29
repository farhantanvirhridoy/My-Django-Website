from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name = "home"),
    path('events', views.event_list, name = 'event_list'),
    path('add_venue', views.add_venue, name = 'add-venue'),
    path('venue_list', views.list_venues, name = 'list-venues'),
    path('show_venue/<venue_id>/', views.show_venue, name = 'show-venue'),
    path('searched_result', views.searching, name = 'searching'),
    path('venue_update_form/<venue_id>/', views.venue_update_form, name = "venue-update-form"),
    path('add_event', views.add_event, name= "add-event"),
    path('event_update_form/<event_id>/', views.event_update_form, name = "event-update-form"),
    path('delete_event/<event_id>/', views.delete_event, name = "delete-event"),
    path('delete_venue/<venue_id>/', views.delete_venue, name = "delete-venue"),
    path('venue_text', views.venue_text, name="venue-text"),
    path('venue_csv', views.venue_csv, name="venue-csv"),
    path('venue_pdf', views.venue_pdf, name="venue-pdf"),
    path('about', views.about, name='about'),
]
