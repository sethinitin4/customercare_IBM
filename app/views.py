from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import User, Complaint
# Create your views here.
def index(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = User.objects.all().filter(username=username).filter(password=password)
        print(user)
        if user is not None:
            request.session['username'] = username
            return redirect('/complaint')
        error='Wrong Username or Password'
    return render(request, 'app/index.html', {"error":error})

def complaint(request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'app/complaint.html')
    else:
        return redirect('/')