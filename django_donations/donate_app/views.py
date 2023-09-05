from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['repeatpassword']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username,email=email,password=password) 
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
