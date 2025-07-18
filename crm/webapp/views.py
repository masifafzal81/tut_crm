from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import RegistrationForm

def home(request):
    
    # check the logged in user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # authenticate the user
    
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        
        else:
            messages.success(request, 'Invalid username or password')
            return redirect('home')        
    
    else:
        return render(request, 'home.html', {})

# def login_view(request):
#     pass
def logout_view(request):
    logout(request)
    messages.success(request, 'You are successfully logged out.')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You are successfully registered and welcome to our site.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})
