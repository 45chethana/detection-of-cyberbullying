from django.shortcuts import render,redirect
from user.models import info

# Create your views here.
def login(request):
    if request.method == "POST":
       if request.method == "POST":
           usid = request.POST['username']
           pswd = request.POST['password']
           if usid == 'admin' and pswd == 'admin':
              return redirect('adminhome')

    return render(request,'adminlogin.html')




def adminhome(request):
    Info=info.objects.all()
    return render(request,"adminhome.html",{"Info":info})
