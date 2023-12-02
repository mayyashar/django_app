from django.urls import path
from playground import views

urlpatterns = [
    path('hello/', views.say_hello_by_name),
    path('hello/', views.say_hello),
    path('',views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('Login', views.Login, name="Login"),
    path('signout', views.signout, name="signout"),
    path('create/', views.create, name="create"),
    path('sent/', views.sent, name='sent'),
    path('super/', views.super, name='super'),
    path('admin_area/', views.admin_area, name='admin_area'),
    path('forbbiden/', views.forbbiden, name='forbbiden'),


    


]
