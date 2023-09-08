from django.shortcuts import render,redirect
from .models import Signup
from django.contrib.auth.models import User,auth
from django.contrib import messages


#is_login = False

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
            return redirect('after_login')
        
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    
    else:
        return render(request,'login.html')   

def after_login(request):
    return render(request, 'after_login.html')     
   

        #   user = CustomUser.objects.get(username=username)
            
        #     # Check the password
        #     if user.check_password(password):
        #         # Password is correct, log in the user
        #         login(request, user)
        #         return redirect('home')  # Redirect to the desired page after login
        #     else:
        #         # Password is incorrect, handle this case (e.g., display an error message)
        #         pass
        # except CustomUser.DoesNotExist    

        # user=auth.authenticate(username=username,password=password)
        
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('index')
        
        # else:
        #     messages.info(request,'Credentials invalid')
        #     return redirect('/')
    
    
        
def logout(request):
    auth.logout(request)
    return redirect('/')

#register code- sai prasad 8.9.23
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['repeatpassword']
        
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,'Email already exists')
#                 return redirect('register')
            
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request,'Username already exists')
#                 return redirect('register')
            
#             else:
#                 user = User.objects.create_user(username=username,email=email,password=password) 
#                 user.save()
#                 return redirect('/')
        
#         else:
#             messages.info(request,'Passwords do not match')
#             return redirect('register')
    
#     else:
#         return render(request,'register.html')

#login code
# def login(request):
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user=auth.authenticate(username=username,password=password)
        
#         if user is not None:
#             auth.login(request,user)
#             return redirect('index')
        
#         else:
#             messages.info(request,'Credentials invalid')
#             return redirect('/')
    
#     else:
#         return render(request,'login.html')