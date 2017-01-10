from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import User, Complaint
import json
from django.http import JsonResponse
import watson_developer_cloud
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
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def viewcomplaints(request):
    complaints = Complaint.objects.all()
tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(username='service credentials - username',password='service credentials - password')    file = open('app/problem2.json')
    k = json.load(file)
    i=0
    obj=[]
    for complaint in complaints:
        obj.append(complaint)
        k['options'].append({'key':i, 'name':complaint.user.username, 'values':{'share':complaint.user.shares, 'urgency':complaint.type, 'aDate':str(complaint.user.reg_data)+"T00:00:00Z"}})
        i=i+1
    dilemma = tradeoff_analytics.dilemmas(k, generate_visualization=False)
    obj1 = []
    obj2 = []
    for s in dilemma['resolution']['solutions']:
        complaint = obj[int(s['solution_ref'])]
        if s['status']=='EXCLUDED':
            obj1.append({'complaint':complaint})
        elif s['status']=='FRONT' :
            obj2.append({'complaint':complaint})
        else:
            return redirect('/failure')
    return render(request,'app/employeeview.html',{'complaints_red': obj2, 'complaints_blue': obj1})
