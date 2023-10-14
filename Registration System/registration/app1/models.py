from django.db import models

# Create your models here.

class UserData(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confirmpassword = models.CharField(max_length=255)
    selected_gender = models.CharField(max_length=10)
    selected_options = models.CharField(max_length=255)
    selected_checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.fname  # Display the first name as a string representation of the object