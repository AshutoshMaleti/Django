from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('loginUser')

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(username,password)

        if user is not None:
            login(user)
            redirect('')
        else:
            return render(request, 'loginUser.html')

    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect('loginUser')