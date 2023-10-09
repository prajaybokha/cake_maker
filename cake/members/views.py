from django.shortcuts import render, redirect
from .models import registers , admin_table
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import login, authenticate


def members(request):
    return render(request,"index.html")

def abcd(request):
    return render(request,"abcd.html")

def contact(request):
    return render(request,"contact.html")
 
'''def register(request):
    return render(request,"register.html")'''

def register(request): 
    mymembers = registers.objects.all().values()
    template = loader.get_template('register.html')
    context = {
        'mymembers' : mymembers
        
    }
    return HttpResponse(template.render(context,request))

def insertrecord(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['password']
    d = request.POST['gender']
    
    member = registers(firstname = a,email = b,password = c,gender = d)
    member.save()
    return HttpResponseRedirect(reverse('login'))

def cake(request):
    return render(request,"cake.html")


def login(request):
    return render(request,"login.html")

def login_user(request):
    if request.method == 'POST':
        email1 = request.POST['ema']
        password1 = request.POST['passw']
        
        try:
            user = registers.objects.get(email=email1,password=password1) 
            if user.email == email1 and user.password == password1:
                return render(request,'index.html')  # Redirect to the home page or any other desired page
            else:
                # Invalid password
                return render(request, 'login.html')
        except:
            pass

    return render(request, 'abcd.html')

def admin_data(request):
    return render(request,"admin_index.html")

def admin_form(request):
    return render(request,"admin_form.html")

def login(request):
    return render(request,"admin_login.html")


def add_data(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['contact']
    d = request.POST['password']
    enter = admin_table(name = a, email = b, contact = c, password = d)
    enter.save()
    return HttpResponseRedirect(reverse('admin_form'))


def admin_checkdata(request):
    if request.method == 'POST':
        email1 = request.POST['login']
        password1 = request.POST['password']
        
        try:
            user = admin_table.objects.get(email=email1,password=password1) 
            if user.email == email1 and user.password == password1:
                return render(request,'admin_index.html')
            else:
                return render(request,'admin_login.html')
        except:
            pass
    return render(request, 'admin_login.html')

def admin_tables(request):
    details = admin_table.objects.all().values()
    template = loader.get_template('admin_tables.html')
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))

def user_data(request):
    details = registers.objects.all().values()
    template = loader.get_template('user_data.html')
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))

def delete(request, id):
    member = admin_table.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('admin_tables'))

def update(request,id):
    info = admin_table.objects.get(id=id)
    template = loader.get_template('admin_update.html')
    context = {
        'info' : info,  
    }
    
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['contact']
    d = request.POST['password']
    member = admin_table.objects.get(id=id)
    member.name=a
    member.email=b
    member.contact=c
    member.password=d
    member.save()
    return HttpResponseRedirect(reverse('admin_tables'))

