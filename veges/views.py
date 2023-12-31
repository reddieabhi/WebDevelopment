from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Sum

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

def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search ) | 
            Q(student_id__student_id__icontains = search ) | 
            Q(student_email__icontains = search ) |
            Q(department__department__icontains = search ) |
            Q(student_age__icontains = search ) 
            )

    paginator = Paginator(queryset,10) # show 10 students lists
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(request,"report/students.html",{"students":page_obj})



def view_student(request,id):
    query_set  = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total = 0
    for i in query_set:
        total += i.marks
    print(total)
    ranks = Student.objects.annotate(marks=Sum('student_marks__marks')).order_by('-marks')   
    current_rank = -1
    temp = 0
    print(ranks[0].student_id)
    for rank in ranks:
        temp += 1
        if str(rank.student_id) == id:
            current_rank = temp
    return render(request,"report/student_marks.html",{'my_marks' : query_set,'total':total,'name':query_set[0].student,'rank':current_rank})

