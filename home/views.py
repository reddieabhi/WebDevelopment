from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .utils import send_email_to_client
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .utils import send_email_to_client


def send_email(request):

    if request.method == 'POST':
        data = request.POST

        subject = data['subject']
        message = data['message']
        send_email_to_client(subject=subject,message=message)

    return render(request,"send_email.html")

def djhtml(request):
    peoples = [
        {'name':'Abhi','age':21},
        {'name':'Reddy','age':20},
        {'name':'Prince','age':22},
        {'name':'Abhiii🍀','age':21}
    ]

    veg = ['a','tomato','chilli','cucmber','brinjal']

    return render(request,"index.html",context={'peoples':peoples})


def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")


def abc(request):
    return HttpResponse(6+5)


def abhi(request):
    return HttpResponse('Hello amma')


def new(request):
    print('new '*100)
    return HttpResponse('this is new')