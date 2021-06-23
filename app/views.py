
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm

# Create your views here.

def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['psw']


        obj = User.objects.create_user(username=username,
                   first_name=first_name,
                   last_name=last_name,
                   email=email,
                   password=password)
        obj.save()
        return redirect('login')
    if request.method == 'GET':

        return render(request,'signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        obj = authenticate(username=username,password=password)
        if obj is not None:
            login(request,obj)
            messages.success(request,('You Have Been Logged In!!'))
            return redirect('home')
        else:
            messages.success(request,('Error Logging In- Please Try Again....'))
            return redirect('login')


    else:
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out...')
    return redirect('login')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have Edited Your Profile...'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form':form}
    return render(request,'edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('Password has been changed'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'change_password.html',context)
