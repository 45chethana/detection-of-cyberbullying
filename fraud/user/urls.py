from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='homepage'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='reg'),
    path('login',views.login,name='log'),
    path('logout',views.logout,name='logout'),
    path('social',views.social_msg,name='social'),
    path('cyberbullying',views.cyberbullying,name='cyberbullying'),
    path('prediction',views.prediction,name='prediction'),
    path('adminlogin',views.prediction,name='adminlogin'),
 
 
 

]

