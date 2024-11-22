from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from .forms import RegisterForm

def frontpage(request):
    # This is your front page view after login
    return render(request, 'Desivibe/frontpage.html')

def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("frontpage"))
        else:
            return render(request, "Desivibe/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Desivibe/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("frontpage"))

 # Import your RegisterForm
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user using the custom RegisterForm
            login(request, user)  # Log in the user after successful registration

            return redirect('frontpage')  # Redirect to your desired page after login (change 'frontpage' to your URL name)
    else:
        form = RegisterForm()
    
    return render(request, 'Desivibe/register.html', {'form': form})
