class Authentication:
    def __init__(self,email,password):
        
        self.email = email
        self.password = password
    def user (self):
        if (self.email == "towhidul101@gmail.com" and self.password == "12345"):
           print("Login Succesfully")
        else:
            print("Email and Password doesn't match")
obj = Authentication("towhidul101@gmail.com","12345")
obj2 = Authentication("towhidul1001@gmail.com","12345")

obj.user()
obj2.user()