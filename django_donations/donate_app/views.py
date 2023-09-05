from django.shortcuts import render,redirect
from .models import Signup
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
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
            if Signup.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            
            elif Signup.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            
            elif Signup.objects.filter(phone_no=phone_no).exists():
                messages.info(request,'Phone number already exists')
                return redirect('register')
            
    
            
            else:
                user = Signup(username=username,email=email,password=password,phone_no=phone_no,address=address) 
                user.save()
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
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        
        else:
            messages.info(request,'Credentials invalid')
            return redirect('/')
    
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")
