from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import os
from .models import form_data


def indexpage(request):
    return render(request, 'index.html')

def homepage(request):
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_phone = request.POST.get('phone')
    u_gender = request.POST.get('gender')
    u_address = request.POST.get("address")
    u_profession = request.POST.get('profession')
    u_education = request.POST.get('education')
    u_course = request.POST.get('course')
    u_photo = request.FILES.get('photo')
    u_transcript = request.FILES.get('transcript')
    
    # Convert the name to uppercase
    u_name = u_name.upper()
    
    user_obj = form_data()
    
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.gender = u_gender
    user_obj.address = u_address
    user_obj.profession = u_profession
    user_obj.education = u_education
    user_obj.course = u_course
    user_obj.photo = u_photo
    user_obj.transcript = u_transcript
    user_obj.save()
    
    messages.success(request, 'Data submitted successfully.')
    
    return redirect ('output')
    

def outputpage(request):
    all_data = form_data.objects.all()
    data = {"user_data": all_data}
    return render(request,'output.html',data)

def backpage(request):
    return redirect('index')

def edit_index(request, id):
    all_data = form_data.objects.get(id=id)
    data = {"user_data": all_data}
    return render(request,'update.html',data)

def update(request):
    id = request.POST.get('id')
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_phone = request.POST.get('phone')
    u_gender = request.POST.get('gender')
    u_address = request.POST.get("address")
    u_profession = request.POST.get('profession')
    u_education = request.POST.get('education')
    u_course = request.POST.get('course')
    
    # Get the user object by ID
    user_obj = get_object_or_404(form_data, id=id)
    
    # Check if new image and video files are provided
    if 'photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if user_obj.photo:
            os.remove(user_obj.photo.path)
        user_obj.photo = request.FILES['photo']
    # Check if new image and video files are provided
    if 'transcript' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if user_obj.transcript:
            os.remove(user_obj.transcript.path)
        user_obj.transcript = request.FILES['transcript']
    
    # Update the other fields    
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.gender = u_gender
    user_obj.address = u_address
    user_obj.profession = u_profession
    user_obj.education = u_education
    user_obj.course = u_course
    user_obj.save()
    return redirect('output')

def delete_index(request, id):
    user_obj = get_object_or_404(form_data, id=id)
    user_obj.delete()
    return redirect('output')
    
    

