from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print('authenticated')
        return render(request, 'index.html')
    else:
        print('not authenticated')
        return redirect('/loginUser')

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        user=authenticate(username=username,password=password)
        print('user auth done')

        if user is not None:
            print('in if')
            login(request, user)
            return redirect('/')
        else:
            print('in else')
            return render(request, 'loginUser.html')

    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect('/loginUser')