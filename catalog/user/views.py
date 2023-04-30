from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    return render(request,'user/login.html')
def register(request):
    if request.method=='POST':

        #get form values
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password == repassword:
            #Username control
            if User.objects.filter(username=username).exists():
                print('This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    print('This email is already taken')
                    return redirect('register')
                else:
                    #everyting clear
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    print('User created')
                    return redirect('login')

        else:
            print('Passwords does not match')
            return redirect('register')
    else:
        return render(request,'user/register.html')
def logout(request):
    return render(request,'user/logout.html')