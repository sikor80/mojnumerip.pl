from django import http
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404

from google.appengine.api import mail

from mainapp.forms import ContactForm

from views_secret import *


def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = {
                'ip': ip,
                }
    return render(request, 'mainapp/index.html', context) 


def mapa(request):
    a = ""
    context = {
            'a': a,
            }
    return render(request, 'mainapp/mapa.html', context)


def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_and_email = "From: " + cd['email'] + " Message: " + cd['message']
            mail.send_mail(sender=SENDER_ADDR,
                          to=TO_ADDR,
                          subject="Wiadomosc z mojnumerip.pl",
                          body=
                          "From: " + cd['email'] 
                          + "\n" +
                          "Subject: " + cd['subject'] 
                          + "\n" + 
                          "Message: " + cd['message'])
            messages.add_message(request, messages.SUCCESS, 'Wiadomosc wysłana. Dziękujemy!')

            return HttpResponseRedirect('/kontakt')
    else:
        form = ContactForm()
    return render(request, 'mainapp/kontakt.html', {'form': form})
