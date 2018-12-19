from django.urls import path
from . import views



urlpatterns = [
    path('events/',views.create_event,name='events'),

]