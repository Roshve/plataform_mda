# Django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .form import FormNewUser
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# Python imports

from datetime import date, datetime

def pages_home(request):
    
    return render(request, 'index.html')

def send_email(data):

    mail = ["mda_lcova@lnexternos.com.ar", "FDeBernardi@lanacion.com.ar", "iprieto@lanacion.com.ar"]
    template = get_template('form/mails/mail.html')
    content = template.render(data)

    d = date.today()
    asunto = d.strftime("Nuevo Ingreso %d-%m-%Y")

    email = EmailMultiAlternatives(
        asunto,
        'Sarasa',
        settings.EMAIL_HOST_USER,
        mail
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def form_news_users(request):

    form = FormNewUser()
    if request.method == 'POST':
        form = FormNewUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_email(data)

    context = {'form':form}
    return render(request, 'form/form_news_users.html', context)