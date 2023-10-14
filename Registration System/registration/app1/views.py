from django.shortcuts import render,HttpResponse,redirect
from app1.models import UserData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views 

def homepage(request):
    return render(request, 'signup.html')
  
def dataget(request):
    fname = ""
    lname = ""
    email = ""
    password = ""
    confirmpassword = ""
    selected_gender = ""
    selected_options = ""
    selected_checkbox = ""

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        selected_gender = request.POST.get('r1')
        selected_options = request.POST.get('occupation')
        selected_checkbox = request.POST.get('checkbox')
        
        # Convert 'selected_checkbox' to a Boolean value
        if selected_checkbox == 'on':
            selected_checkbox = True
        else:
            selected_checkbox = False
        
        if password != confirmpassword:
           return HttpResponse("Password and Confirm Passwor are not same")
        else:
            values = UserData(
                fname=fname,
                lname=lname,
                email=email,
                password=password,
                confirmpassword=confirmpassword,
                selected_gender=selected_gender,
                selected_options=selected_options,
                selected_checkbox=selected_checkbox
            )
            values.save()
    return redirect('login')

    # data = {
    #     "fname": fname,
    #     "lname": lname,
    #     "email": email,
    #     "password": password,
    #     "confirmpassword": confirmpassword,
    #     "selected_gender": selected_gender,
    #     "selected_options": selected_options,
    #     "selected_checkbox": selected_checkbox
    # }

    

def signuppage(request):
    pass
   

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserData.objects.get(email=email, password=password)
            # If a user with the provided email and password is found
            return redirect('index')
        except UserData.DoesNotExist:
            # If no user with the provided credentials is found
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
        

        
def indexpage(request):

     return render(request,'index.html')
 
def logoutpage(request):
    logout(request)
    return redirect('login')