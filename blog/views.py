from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.http import HttpResponse

def home(request):
    output = '\n'.join([
        _("Welcome to my site."),  # Translators: New string in our site
        _("Arabic"),  # Transltors: Built-in in Django
        _("Django"),  # Translators: New string in our site
        _("Home"),  # Transltors: Built-in in Django
    ])

    return HttpResponse(output, content_type='text/plain; charset=utf-8')

def walli(request):
    return render(request, 'walli.html', {
        'home': _("Home"),  # Transltors: Built-in in Django
    })
