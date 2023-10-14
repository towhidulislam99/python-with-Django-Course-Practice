from django.db import models


class form_data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    profession = models.CharField(max_length=500)
    education = models.CharField(max_length=500)
    course = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/', default='No images')
    transcript = models.ImageField(upload_to='images/', default='No images')
    