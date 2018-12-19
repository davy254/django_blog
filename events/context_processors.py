from .models import Events

def processor(request):
    events = Events.objects.all().order_by('date1')
    return {'event_list':events}



