from courseapp.models import SiteEvents


def get_events(request):
    all_events = SiteEvents.objects.all()
    return {'all_events': all_events}
