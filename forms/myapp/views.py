from django.shortcuts import render
from .models import User
from.forms import LoginForm
import requests

# Create your views here.
#login_out
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST['phone']
        user = authenticate(request, email=email, phone=phone)
        if email and phone is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your home URL path

    return render(request, './login.html')
def home(request):
    return render(request, './home.html')
def login(request):
    return render(request, './login.html')