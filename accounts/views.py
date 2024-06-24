from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def  admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def user_register(request):
    return render(request, 'user_register.html')

def user_login(request):
    return render(request, 'user_login.html')

def user_logout(request):
    return render(request, 'user_logout.html')