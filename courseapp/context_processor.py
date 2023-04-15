import datetime

from courseapp.models import SiteEvents


def get_events(request):
    all_events = SiteEvents.objects.filter(end_time__gt=datetime.datetime.now())
    return {'all_events': all_events}
