from django.urls import path
from playground import views

urlpatterns = [
    path('hello/', views.say_hello_by_name),
    path('hello/', views.say_hello),
    path('',views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('Login', views.Login, name="Login"),
    path('signout', views.signout, name="signout"),
    path('create/', views.create, name="creat"),

]
