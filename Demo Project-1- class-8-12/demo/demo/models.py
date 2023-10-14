from django.db import models

class demo_user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    video = models.FileField(upload_to='videos/',default='No Videos')