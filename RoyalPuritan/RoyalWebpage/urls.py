from django.urls import path 
from . import views 
from .views import slideshow_view
from django.contrib.auth import views as auth_views

urlpatterns = [ 
	path("", views.home, name="home"), 
    # path('slideshow/', views.slideshow_view, name='slideshow'),
	path('projects/', views.projects, name="projects"), 
	path('contact/', views.contact, name="contact"), 
    path('about/', views.about, name='about'),
    path('banner/', views.banner, name='banner'),
    path('slideshow/', slideshow_view, name='slideshow'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('secondBanner/', views.secondBanner, name='secondBanner'),
    path('testimonials/', views.all_testimonials, name='all_testimonials'), 
    path('submit/', views.submit_testimonial, name='submit_testimonial')
    
    
]
