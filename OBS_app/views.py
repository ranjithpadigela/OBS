from django.shortcuts import render, redirect
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
    return render(request, 'adminpage.html')

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

def Addbook(request):
    return render(request,'addbook.html')

def addbook(request):
    b_id = request.GET['t1']
    btitle = request.GET['t2']
    bauthor = request.GET['t3']
    bprice = request.GET['t4']
    bedition = request.GET['t5']
    bdate = request.GET['t6']
    #bimage = request.POST['b5']
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
    return redirect('/')
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



