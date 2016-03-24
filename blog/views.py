from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.http import HttpResponse

def home(request):
    output = ' '.join([
        _("Welcome to my site."),  # Translators: New string in our site
        _("Arabic"),  # Transltors: Built-in in Django
        _("Django"),  # Translators: New string in our site
        _("Home"),  # Transltors: Built-in in Django
    ])

    return HttpResponse(output)
