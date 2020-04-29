from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import *

# Create your views here.
def Login(request):
    error=False
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error=True
    return render(request,'loginform.html',{"error":error})

def Logout(request):
	logout(request)
	return redirect('login')

def indexpage(request):
    data=donate.objects.all()
    if request.method=='POST':
        name=request.POST["name"]
        father_name=request.POST["father_name"]
        group=request.POST["group"]
        hos=request.POST["hos"]
        date=request.POST["date"]
        mobile=request.POST["mobile"]
        donate.objects.create(name=name,father_name=father_name,group=group,hos=hos,date=date,mobile=mobile)
        return redirect('home')
    return render(request,'index.html',{"data":data})

def reg(request):
    user=User.objects.all()
    data=user
    user_taken = False
    email_taken = False
    password_match = False
    if request.method=='POST':
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                user_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            elif User.objects.filter(email=email).exists():
                email_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=fname,last_name=lname,)
                user.save()
                print('user created')
        else:
            password_match=True
            return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})

        return redirect('reg')
    return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
    

def bloodreq(request):
    data=bloodrequest.objects.all()
    if request.method=='POST':
        name=request.POST["name"]
        fathername=request.POST["fathername"]
        group=request.POST["group"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        bloodrequest.objects.create(name=name, fathername=fathername, group=group, email=email,phone=phone,  address=address)
        return redirect('bloodreq')
    return render(request,'bloodreq.html',{'data':data})

def viewreq(request):
    data=bloodrequest.objects.all()
    return render(request,'viewreq.html',{'data':data})

def donateblood(request):
    data=addhospital.objects.all()
    if request.method=='POST':
        name=request.POST["name"]
        fathername=request.POST["fathername"]
        hospital=request.POST["hospital"]
        group=request.POST["group"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        donate.objects.create(name=name, fathername=fathername,hospital=hospital,group=group,email=email,phone=phone,address=address)
    return render(request,'donateblood.html',{'data':data})

def search(request):
    data=donate.objects.all()
    return render(request,'search.html',{'data':data})

def Addhospital(request):
    data=addhospital.objects.all()
    if request.method=='POST':
        hospital=request.POST["hospital"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        addhospital.objects.create(hospital=hospital,address=address,phone=phone)
        return redirect('addhospital')
    return render(request,'addhospital.html',{"data":data})
    

def viewhospital(request):
    data=addhospital.objects.all()
    return render(request,'viewhospital.html',{'data':data})


def Edit_Delete_hospital(request,sid,option):
    data=addhospital.objects.filter(id=sid).first()
    if option=='Delete':
        data.delete()
        return redirect('viewhospital')
    if option =='Edit':
        if request.method=='POST':
            data.hospital=request.POST['hospital']
            data.address=request.POST['address']
            data.phone=request.POST['phone']
            data.save()
            return redirect('viewhospital')
        return render(request,'viewhospital.html',{'data':data})

def message(request,sid,option):
    data=bloodrequest.objects.filter(id=sid).first()
    if option=='Accept':
        
        subject = 'Today Your Bus Detail'
        message = ' Hello'+" "+ str(data.name)+" "+' your request is accepted.' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [str(data.email)]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('viewreq')
    if option=='Dismiss':
        
        subject = 'Today Your Bus Detail'
        message = ' Hello'+" "+ str(data.name)+" "+' your request is rejected.' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [str(data.email)]
        send_mail( subject, message, email_from, recipient_list )
        data.delete()
        return redirect('viewreq')