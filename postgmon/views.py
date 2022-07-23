from django.shortcuts import render, redirect
from .models import postgmodels
from .forms import postgform, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .decorators import allowed_users



def loginpage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password is incorrect")
            return redirect('/')

    return render(request, 'login.html') 

def logoutuser(request):
    logout(request)
    return redirect('/') 


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') #this line harvests the name of the user
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'register.html', context)  


#@login_required(login_url='loginpage') #this prevents anyone from just using restricted url to access the page
#@allowed_users(allowed_roles=['customer'])
def home(request):
    #if request.user.groups.filter(name='customer').exists(): #these 2 lines have to be repeated to do permission the manual way
    flura = postgmodels.objects.all()

    

    #elif request.user.groups.filter(name='admin').exists():
        
        #flura = postgmodels.objects.all()

    floxy = postgform()
    if request.method == "POST":
        floxy = postgform(request.POST)
        if floxy.is_valid():
            tiler = floxy.save(commit=False)
            tiler.author = request.user
            tiler.save()
            
    #else:
        #return HttpResponse(' you are not allowed to view this page, only for priviledged users')

    context = {'flura':flura, 'floxy':floxy}            
    return render(request, 'home.html', context)
   


def userpage(request):
    if request.user.is_authenticated:
        return render(request, 'user.html')
    else:
        return HttpResponse('Seems you do not have an account yet!, please go back to register')
    context = {}
    return render(request, 'user.html', context)

    
def update(request, pk):
    cisa = postgmodels.objects.get(id=pk)

    floxy = postgform(instance=cisa)
    if request.method == "POST":
        floxy=postgform(request.POST, instance=cisa)
        if floxy.is_valid():
            floxy.save()
            return redirect('home')
    context={'cisa':cisa, 'floxy':floxy}
    return render(request, 'update.html', context)

def delete(request, pk):
    cisa = postgmodels.objects.get(id=pk)

    if request.method == "POST":
        cisa.delete()
        return redirect('home')
    context={'cisa':cisa}
    return render(request, 'delete.html', context)


