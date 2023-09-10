from django.shortcuts import render,redirect
from .models import Signup
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.urls import clear_url_caches


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone_no = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        # city = request.POST['Select_City']
        password = request.POST['password']
        password2 = request.POST['repeatpassword']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            
            elif Signup.objects.filter(phone_no=phone_no).exists():
                messages.info(request,'Phone number already exists')
                return redirect('register')
            
    
            
            else:
                user = Signup(username=username,email=email,password=password,phone_no=phone_no,address=address) 
                user1 = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user1.save()
                return redirect('/')
        
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
    
    else:
        return render(request,'register.html')
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            #is_login=True
            return redirect('after_login')
        
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    
    else:
        return render(request,'login.html')   
    

@login_required
def after_login(request):
    
    return render(request, 'after_login.html')
        # Perform actions for authenticated user
    #return render(request, 'after_login.html')     
  
def logout(request):
    #clear_url_caches()
    auth.logout(request)
    #clear_url_caches()
    return redirect('/')
