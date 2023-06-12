from django.shortcuts import render
from .models import Privacy


def privacy(request):
    """ Display privacy page """
    privacy = Privacy.objects.all()

    context = {
        'privacy': privacy
    }
    template_name = 'privacy/privacy.html'
    return render(request, template_name, context)
