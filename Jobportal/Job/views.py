from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no" 
            else:
                error="yes" 
        except:
            error="yes" 
    d = {'error':error}
    return render(request,'admin_login.html',d)

def user_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = CandidateUser.objects.get(user=user)
                if user1.type == "candidate":
                    login(request,user)
                    error="no" 
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'user_login.html',d)

def recruiter_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = RecruiterUser.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="pending":
                    login(request,user)
                    error="no" 
                else:
                    error="not"
            except:
                    error="yes"
        else:
            error="yes"
    d = {'error':error}    
    return render(request,'recruiter_login.html' ,d)

def recruiter_signup(request):
    error = ""
    if request.method=='POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        i = request.FILES.get('img')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        c = request.POST.get('mobile')
        g = request.POST.get('gender')
        cp = request.POST.get('company')
        try:
            user = User.objects.create_user(first_name=f, last_name=l,username=e,password=p)
            RecruiterUser.objects.create(user=user,mobile=c,image=i,gender=g,company=cp, type="recruiter",status="pending")
            error="no"
        except:
            error="yes"
    d = {'error':error}   
    return render(request,'recruiter_signup.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request,'recruiter_home.html')
def Logout(request):
    logout(request)
    return redirect('index')


def user_signup(request):
    error = ""
    if request.method=='POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        i = request.FILES.get('img')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        c = request.POST.get('mobile')
        g = request.POST.get('gender')
        try:
            user = User.objects.create_user(first_name=f, last_name=l,username=e,password=p)
            CandidateUser.objects.create(user=user,mobile=c,image=i,gender=g, type="candidate")
            error="no"
        except:
            error="yes"
    d = {'error':error}   
    return render(request, 'user_signup.html',d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = CandidateUser.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    candidate = CandidateUser.objects.get(id=pid)
    candidate.delete()
    return redirect('view_users')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = RecruiterUser.objects.filter(status='pending')
    d = {'data':data}
    return render(request,'recruiter_pending.html',d)

