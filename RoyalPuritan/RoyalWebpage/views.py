from django.shortcuts import render, redirect
# import requests
from .models import SlideshowImage
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required
from django.conf import settings    # Import the settings file
# views.py

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def profile(request): 
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')  # Redirect to the profile page after login
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def home(request):
    testimonials = Testimonial.objects.all()[:3] # Limit to 3 testimonials for homepage
    return render(request, 'home.html', {'testimonials': testimonials})


def home(request):
    images = SlideshowImage.objects.all()
    testimonials = Testimonial.objects.all()[:3] # Limit to 3 testimonials for homepage
    return render(request, 'home.html', {'testimonials': testimonials, 'images':images })


    
   
   
   
    

   


def slideshow_view(request):
    images = SlideshowImage.objects.all()
    return render(request, 'slideshow.html', {'images': images})

def about(request):
    return render(request, 'about.html')


def secondBanner(request):
    return render(request, 'secondBanner.html')

def banner(request):
    return render(request, 'banner.html')

def mission(request):
    return render(request, 'home.html#mission')

def contact(request):
    return render(request, 'contact.html')  

def projects(request):
    return render(request, 'projects.html')
# Create your views here.



def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
             testimonial = form.save(commit=False) 
             testimonial.user = request.user 
             testimonial.save()
             return redirect('home') 
        else: form = TestimonialForm()
        return render(request, 'submit_testimonial.html', {'form': form})



def all_testimonials(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            return redirect('all_testimonials')
    else:
        form = TestimonialForm()
    
    testimonials = Testimonial.objects.all()
    return render(request, 'all_testimonials.html', {'testimonials': testimonials, 'form': form})
