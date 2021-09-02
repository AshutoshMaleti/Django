from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginUser(request):
    return render(request, 'loginUser.html')

def logoutUser(request):
    #return render(request, 'logoutUser.html')
    return HttpResponse('logged out')