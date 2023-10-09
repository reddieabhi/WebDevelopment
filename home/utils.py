from home.models import Student
import time
from django.core.mail import send_mail
from django.core.mail import *
from django.core.mail import backends
from django.core.mail.backends import smtp
from django.conf import settings


def send_email_to_client(subject,message):
    
    from_email = settings.EMAIL_HOST_USER
    recipeint_list = ["babhinayreddy2001@gmail.com","bmanideepreddy2@gmail.com"]
    send_mail(subject,message,from_email,recipeint_list)

