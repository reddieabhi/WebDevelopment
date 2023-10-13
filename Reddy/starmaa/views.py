from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import *



def working(request):
    return HttpResponse('working')

def userdata(request):

    if request.method == 'POST':
        data = request.POST
        fname = data['fname']
        lname = data['lname']
        if fname and lname:
            People.objects.create(fname=fname,lname=lname)
        
        return redirect('/user')
    
    people = People.objects.all()
    context = {'people':people}


    return render(request,"People.html",context)


