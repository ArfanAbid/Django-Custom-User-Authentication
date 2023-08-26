from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from Authentication.models import CustomUser
from django.contrib import messages # for desplaing necessary messages The user
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')





def register(request):
    if request.method == 'POST':
        first=request.POST.get('first_name')
        last=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('/Register')
        

        
        RegisterUser=CustomUser(first_name=first,last_name=last,email=email)
        RegisterUser.set_password(password)
        RegisterUser.save()
        # OR
        # RegisterUser=CustomUser.objects.create_user(email=email, password=password, first_name=first, last_name=last)  # it is definef in manager.py 
        # RegisterUser.set_password(password)
        # RegisterUser.save()
        
        messages.info(request, "Account Created SuccessFully")
        return redirect('/Register')
        
    return render(request, 'Register.html')








def login_user(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if  not CustomUser.objects.filter(email=email).exists():
            messages.info(request, "Invalid  @Email  !!!")
            return redirect('/Login')

        user=authenticate(request,email=email,password=password)
        
        if user is None:
            messages.info(request, "Invalid  Password  !!!")
            return redirect('/Login')
        else:
            login(request,user)
            return redirect('/Blog')
        
        
    return render(request, 'login.html')





def logout_page(request):
    logout(request)
    return redirect('/Login')




@login_required(login_url="/Login")
def blog(request):
    return render(request, 'Blog.html')