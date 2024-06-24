from django.shortcuts import render,redirect
from django.contrib import messages



# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_profile(request):
    return render(request, 'admin_profile.html')
