from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login_page")
def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data['receipe_name'] 
        receipe_description = data['receipe_description']
        receipe_image = request.FILES.get('receipe_image')
        if receipe_name != 'chiken':

            
            Receipe.objects.create(
                    receipe_name = receipe_name,
                    receipe_description = receipe_description,
                    receipe_image = receipe_image
                )
        else:
            return HttpResponse('only veg is allowed, non veg is not a valid receipe')
            
        
        return redirect("/receipes")
        
    query_set = Receipe.objects.all()

    if request.GET.get('search'):
        query_set = query_set.filter(receipe_name__icontains = request.GET.get('search'))
    
    context = {"receipes":query_set}     

    return render(request,"receipes.html",context)

@login_required(login_url="/login_page  ")
def delete_reciepe(request,id):
    print(id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()

    return redirect('/receipes')

@login_required(login_url="/login_page  ")
def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        receipe_name = data['receipe_name'] 
        receipe_description = data['receipe_description']
        receipe_image = request.FILES.get('receipe_image')
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipes')
    context = {'receipe':queryset}
    return render(request,'update_receipe.html',context)

def exist(request):
    return render(request,"Receipe_existed.html")


def login_page(request):
    if request.method == "POST":
        data = request.POST
        Username = data['user_name']
        Password = data['user_password']


        if not User.objects.filter(username = Username):
            messages.error(request,"Invalid Username")
            return redirect("/login_page")
        
        user = authenticate(username = Username,password = Password)
        if user is None:
            messages.error(request,"Incorrect password")
            return redirect("/login_page")
        else:
            login(request,user)
            return redirect("/receipes")


    return render(request,"login.html")



def logout_page(request):
    logout(request)
    return redirect('/login_page')

def register(request):
    if request.method == "POST":
        data = request.POST
        Username = data['Username']
        Firstname = data['Firstname']
        Lastname = data['Lastname']
        Password = data['Password']

        user = User.objects.filter(username = Username)  
        if user.exists():
            messages.info(request,"Username has already taken")
            return redirect('/register')

        
        user = User.objects.create(
            first_name = Firstname,
            last_name = Lastname,
            username = Username
        )
        user.set_password(Password)
        user.save()
        messages.info(request,"Account created succesfully")

        return redirect('/register')
    
    return render(request,"register.html")

