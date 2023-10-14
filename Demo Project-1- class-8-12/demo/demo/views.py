from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import demo_user
from django.contrib import messages
import os

def index(request):
    all_data = demo_user.objects.all()
    data = {"user_data": all_data}
    return render(request,'demo.html',data)
def user(request):
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_image = request.FILES.get('image')
    u_video = request.FILES.get('video')
    
    user_obj = demo_user()
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.image = u_image
    user_obj.video = u_video
    user_obj.save()
    return redirect('demo_index')

def edit_index(request, id):
    all_data = demo_user.objects.get(id=id)
    data = {"user_data": all_data}
    return render(request,'edit.html',data)
   
    
def update(request):
    id = request.POST.get('id')
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    
    # Get the user object by ID
    user_obj = get_object_or_404(demo_user, id=id)
    
    # Check if new image and video files are provided
    if 'image' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if user_obj.image:
            os.remove(user_obj.image.path)
        user_obj.image = request.FILES['image']
    
    if 'video' in request.FILES:
        # If a new video is provided, delete the old one if it exists
        if user_obj.video:
            os.remove(user_obj.video.path)
        user_obj.video = request.FILES['video']
    
    # Update the other fields
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.save()
    
    return redirect('demo_index')

def delete_index(request, id):
    user_obj = get_object_or_404(demo_user, id=id)
    user_obj.delete()
    return redirect('demo_index')