from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render (request,'index.html')
def user(request):
    name  = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
   
    data = {
        "user":name,
        "email":email,
        "password":password
    }
    
    return render (request,'output.html',data)
