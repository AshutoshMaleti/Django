from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginUser',views.loginUser,name='loginUser'),
    path('logoutUser',views.logoutUser,name='logoutUser')
]