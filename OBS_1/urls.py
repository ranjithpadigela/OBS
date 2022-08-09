"""OBS_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OBS_app.views import *
admin.site.site_header = "Online Book Store Admin"
admin.site.site_title  = "Online Book Store Portal"
admin.site.index_title = "Welcome to Online Book Store"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('adminhome',Adminhome,name='adminhome'),
    path('Addingbook',Addbook,name='Addingbook'),
    path('Addingbook/Addbook',addbook,name='addbookmsg'),
    path('updateinput',Updateinput,name='updateinput'),
    path('updateinput/update/',Update,name='update'),
    path('deleteinput',Deleteinput,name='deleteinput'),
    path('deletebook',Deletebook,name='deletebook'),
    path('addtocart/<str:pk>/',addtocart,name='addtocart'),
    path('remove/<str:pk>/', Removecart, name='remove'),
    path('viewcart',viewcart,name='viewcart'),
    path('signup',signup,name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('adminpage',Adminpage,name='adminpage'),
    path('customerpage',Customerpage,name='customerpage'),
    path('orderpage/<str:pk>/',Buy,name='Buy'),
    path('AddingAdress',AddingAdress,name='Addrs'),
    path('Contactpage',contactUs,name='ContactUs'),
    path('Aboutuspage',AboutUs,name='AboutUs')
]