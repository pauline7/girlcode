from django.urls import path
from . import views

app_name = 'girlchat'  #to be able to add this url to another app, changes also on urls.py

urlpatterns = [
    path('',views.chat, name='chat'),
    #path('login',views.login, name='login'),
    #path('register',views.register, name='register'),
    #path('logout',views.logout, name='logout'),

]