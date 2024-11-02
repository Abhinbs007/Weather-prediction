
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import uuid
from django.contrib.auth.decorators import login_required
from .models import Feedback

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:

           

            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken*")
                return redirect("register")

            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")

        else:
            messages.info(request, "Password is not matching ")
            return redirect('register')

        return redirect('/')  #To redirect to home

    else:
        return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            uid=str(uuid.uuid4())  #GEnerate a random UID
            request.session['uid'] = uid  #Add the UID to the session
            request.session['username']=username #Adding email to session
            return redirect('/')
        else:
            messages.info(request,'Invalid details')
            return redirect('login')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/') 



def about(request):
    return render(request,'about.html')

@login_required
def feedback_view(request):
    if request.method == 'POST':
        message = request.POST['message']
        rating = int(request.POST['rating'])
        
        # Create feedback entry
        Feedback.objects.create(user=request.user, message=message, rating=rating)
        
        messages.success(request, 'Thank you for your feedback!')
        return redirect('home')
    
    return render(request, 'feedback.html')

def home_view(request):
    return render(request, 'base.html')  # Assuming your base template contains the main content
