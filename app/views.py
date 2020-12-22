from django.shortcuts import redirect,render
import random
from django.http import JsonResponse
from .models import Patient
from django.views.generic import ListView , DetailView
from twilio.rest import Client
from datetime import datetime
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
import os

import json
# Create your views here.

account_sid = 'your_twilio_sid'
auth_token = 'your_twilio_token'
my_number = 'your_twilio_number'
client = Client(account_sid, auth_token)


class HomePageView(ListView):
    template_name = 'index.html'
    model = Patient
    context_object_name = 'patients'

    def get_queryset(self):
        patients = super().get_queryset()
        if not self.request.user.is_authenticated:
            return None
        return patients

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        url = staticfiles_storage.path('quicktext.csv')
        df = pd.read_csv(url)
        context['all'] = zip(df['quick'].to_list(),df['complete'].to_list())
        return context


def send_message(request):
    msg = request.GET.get('msg')
    to = request.GET.get('to')
    client.messages \
        .create(
            body=msg,
            from_=my_number,
            to=to
        )
    return JsonResponse({})


def show_detail(request):
    number = request.GET.get('id')
    this_p = Patient.objects.filter(phone_number=number)[0]
    return JsonResponse({'firstname': this_p.firstname,
                         'lastname': this_p.lastname,
                         'gender': this_p.gender,
                         'dob': datetime.strftime(this_p.date_of_birth,'%m-%d-%Y'),
                         'phone_number': this_p.phone_number,
                         'email': this_p.email
                         })


def specialDiv(request):
    number = request.GET.get('id')
    messages = get_messages(number)
    this_p = Patient.objects.filter(phone_number=number)
    p_name = this_p[0].firstname + " " + this_p[0].lastname
    return JsonResponse({'data1': random.randint(0, 20),'data2':number,'messages':messages,'name':p_name})


def get_messages(number):
    sent = client.messages.list(from_=my_number, to=number)
    received = client.messages.list(from_=number, to=my_number)
    messages = sent+received

    my_messages = {}
    i = 0
    for record in messages[::-1]:
        my_messages[record.sid] = {}
        my_messages[record.sid]['sid'] = record.sid
        my_messages[record.sid]['msg'] = record.body
        my_messages[record.sid]['sender'] = 'me' if record.from_ == my_number else 'you'
        my_messages[record.sid]['datetime'] = datetime.strftime(record.date_sent, "%m-%d-%y %H:%M")
        i += 1

    res = sorted(my_messages.items(), key=lambda x: x[1]['datetime'])
    chats = {k: v for k, v in res}
    return chats


def save_patient(request):
    if request.method == "POST":
        Patient(firstname=request.POST.get("firstname"),
                lastname=request.POST.get("lastname"),
                gender=request.POST.get("gender"),
                email=request.POST.get("email"),
                phone_number=request.POST.get("phone_number"),
                date_of_birth=datetime.strptime(request.POST.get("date_of_birth"), '%m-%d-%Y'),
                added_by=request.user.username,
                ).save()
    return redirect('/')


def add_quicktext(request):
    abb = request.POST.get('Abbr')
    txt = request.POST.get('Text')
    url = staticfiles_storage.path('quicktext.csv')

    df = pd.read_csv(url)

    df.loc[len(df.index)] = [abb, txt]

    df.to_csv(url, index=False)

    return redirect('/')

