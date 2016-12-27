from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import User, Complaint
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user is not None:
            request.session['username'] = username
            return redirect('/complaint')
        error='Wrong Username or Password'
    return render(request, 'app/index.html', {"error":error})

def complaint(request):
    if 'username' in request.session and request.session['username'] is not None:
        if request.method == 'POST':
            try:
                description = request.POST['description']
                type = request.POST['type']
            except e:
                return redirect('/failure')
            c = Complaint(user=User.objects.filter(username=request.session['username']).first(), description=description, type=type)
            try:
                c.save()
            except e:
                return redirect('/failure')
            return redirect('/success')
        return render(request, 'app/complaint.html')
    else:
        return redirect('/')

def success(request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'app/success.html')
    else:
        return redirect('/')

def failure(request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'app/failure.html')
    else:
        return redirect('/')

def Logout(request):
    if 'username' in request.session and request.session['username'] is not None:
        request.session.pop('username')
        return redirect('/')
    else:
        return redirect('/')
def Login(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/viewcomplaints')
            else:
                error = "Wrong Username or Password"
        else:
            error = "Wrong Username Or Password"
    return render(request, "app/login.html", {'error':error})

@login_required(login_url='/login')
def LogoutEmployee(request):
    logout(request, user)
    return redirect('/login')

@login_required(login_url='/login')
def viewcomplaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'app/employeeview.html', {'complaints':complaints})