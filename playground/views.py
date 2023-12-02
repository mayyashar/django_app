from imaplib import _Authenticator
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import BadHeaderError
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login, logout
from .forms import createNewList
from django.contrib.auth.decorators import login_required
from .models import FormData


# Create your views here.
def say_hello(request):
    return HttpResponse('hello world')

def say_hello_by_name(request):
    return render(request, 'fronted.html', {'name':'Omri'})

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username=request.POST['username']    
        fname=request.POST['fname'] 
        lname=request.POST['lname'] 
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
                
                
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        

        myuser=User.objects.create_user(username, email, pass1)
        myuser.firstname=fname
        myuser.lasttname=lname

        myuser.save()

        messages.success(request,"your account has seccesfully created")

        return redirect(Login)

    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        username=request.POST['username']    
        pass1=request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request, 'index.html', {'fname':fname})
        else:
            messages.error(request,"bad credentials!")
            return redirect ('home')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def sent(request):
    return render(request, 'sent.html')

def create(request):
    if request.method == "POST":
        form = createNewList(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.save()
            return redirect('sent')
            
        # Your form processing logic here
        else:
            print(form.errors)
            return render(request, 'create.html', {'form': form})
    else:
        form = createNewList()
        return render(request, 'create.html', {'form': form})





  
   
# def create(response):
#     if response.method =="POST":
#         form= createNewList(response.POST)
#     else:
#         form= createNewList()
#     return render(response, 'create.html', {'form':form})

