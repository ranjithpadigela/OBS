from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'Home.html', context)

def Adminpage(request):
    return render(request, 'adminpage')

def Adminhome(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request,'Adminhome.html',context)

def Customerpage(request):
    return render(request,'customer.html')

def signup(request):
    form = CreateUserForm()
    cust_form = createcustomerform()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        cust_form = createcustomerform(request.POST)
        if form.is_valid() and cust_form.is_valid():
            user = form.save()
            customer = cust_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('signin')
    context = {
        'form': form,
        'cust_form': cust_form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            qs = User.objects.filter(is_staff=True, username=username)
            if qs:
                login(request, user)
                return redirect('adminpage')
            else:
                login(request, user)
                return redirect('customerpage')
    context = {}
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')

def contactUs(request):
    return render(request,'contactus.html')

def Addbook(request):
    return render(request,'addbook.html')

def AboutUs(request):
    return render(request,'aboutus.html')

def addbook(request):
    b_id = request.GET['t1']
    btitle = request.GET['t2']
    bauthor = request.GET['t3']
    bprice = request.GET['t4']
    bedition = request.GET['t5']
    bdate = request.GET['t6']
    #bimage = request.POST['t7']
    b = Book(bid=b_id,title=btitle,Author=bauthor,Price=bprice,Edition=bedition,pub_date=bdate)
    b.save()
    return render(request,'bookadmsg.html')

def Updateinput(request):
    return render(request,'updatebook.html')

def Update(request):
    b_id = int(request.GET["t1"])
    b_name = request.GET["t2"]
    b_author = request.GET["t3"]
    b_cost = float(request.GET["t4"])
    b_edition = request.GET['t5']
    b_pdate = request.GET["t6"]
    B=Book.objects.get(bid=b_id)
    B.title=b_name
    B.Price=b_cost
    B.Author=b_author
    B.Edition = b_edition
    B.pub_date=b_pdate
    B.save()
    resp = HttpResponse("product updated successfully")
    return resp
def Deleteinput(request):
    return render(request,'Delete.html')

def Deletebook(request):
    b_id = int(request.GET['t1'])
    book = Book.objects.get(bid=b_id)
    book.delete()
    return HttpResponse("The book has been deleted successfully")


def addtocart(request, pk):
    book = Book.objects.get(bid=pk)
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        carts = Cart.objects.all()
        reqcart = ''
        for cart in carts:
            if (cart.customer == c):
                reqcart = cart
                break
        if (reqcart == ''):
            reqcart = Cart.objects.create(
                customer=c,
            )
        reqcart.books.add(book)
        messages.success(request,"Added to cart")
    return redirect('/')

def Removecart(request, pk):
    book = Book.objects.get(bid=pk)
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        carts = Cart.objects.all()
        for cart in carts:
            if (cart.customer == c):
                reqcart = cart
                break
        if (reqcart == ''):
            reqcart = Cart.objects.delete(
                customer=c,
            )
        reqcart.books.remove(book)
        if reqcart == '':
            return render(request,'emptycart.html')
    return redirect('viewcart')


def viewcart(request):
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        carts = Cart.objects.all()
        for cart in carts:
            if (cart.customer == c):
                context = {
                    'cart': cart
                }
                return render(request,'viewcart.html',context)
            else:
                return render(request,'emptycart.html')


def Buy(request,pk):
    book = Book.objects.get(bid=pk)
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        Order = Orders.objects.all()
        for od in Order:
            if (od.customer == c):
                reqcart = od
        #reqcart.book.add(book)
    return render(request,'Order.html')

def AddingAdress(request):
    name = request.POST['username']
    Aphone = request.POST['phone']
    Apincode = request.POST['pincode']
    ALocality = request.POST['locality']
    Aaddress = request.POST['Address']
    Acity = request.POST['cityDistrictTown']
    Astatelist = request.POST['statelist']
    ALandmark = request.POST['Landmark']
    Aaltphone = request.POST['AlternatePhone']

    A = DeliverAddress(username=name,phone=Aphone,pincode=Apincode,Locality=ALocality,Address=Aaddress,cityDictrictTown=Acity,state=Astatelist,Landmark=ALandmark,Alternate_phone=Aaltphone)
    A.save()
    return HttpResponse("Thank you for purchasing")