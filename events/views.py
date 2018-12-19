from django.shortcuts import render
from .forms import EventsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import Events
from django.views.generic import ListView

# Create your views here.
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventsForm(request.POST)

        if form.is_valid():
            form.save()
            new_date = form.cleaned_data.get('date')
            Events.date1 = new_date



            messages.success(request, f'Event has been created!')


            return redirect('events')

    else:
        form = EventsForm()

    return render(request, 'events/events.html', {'form': form})



