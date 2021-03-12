# Django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .form import FormBaterias
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# Python imports

from datetime import date, datetime


def send_email(data):

    mail = str("mda_lcova@lnexternos.com.ar")
    template = get_template('garantias/mails/mail.html')
    content = template.render(data)

    d = date.today()
    asunto = d.strftime("Garantias %d-%m-%Y")

    email = EmailMultiAlternatives(
        asunto,
        'Sarasa',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def index(request):

    form = FormBaterias()
    if request.method == 'POST':
        form = FormBaterias(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_email(data)

    context = {'form':form}
    return render(request, 'garantias/garantias.html', context)
