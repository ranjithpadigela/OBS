from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,null=True)
    Author = models.CharField(max_length=200, null=True)
    Price = models.DecimalField(max_digits=12,decimal_places=4)
    #book_pic = models.ImageField(null=True, blank=True)
    Edition = models.IntegerField()
    pub_date = models.DateField()
    #Image =models.ImageField()

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    cname = models.CharField(max_length=200,null=True)
    cphone = models.CharField(max_length=200,null=True)
    cemail = models.CharField(max_length=200,null=True)
    cAddress = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    cdate_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.cname)


class Cart(models.Model):
    customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return str(self.customer)

class Orders(models.Model):
    orderid = models.IntegerField()
    books = models.ManyToManyField(Book)
    def __str__(self):
        return str(self.books)

class DeliverAddress(models.Model):
    username = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10,null=True)
    pincode = models.CharField(max_length=6,null=True)
    Locality = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=200,null=True)
    cityDictrictTown = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    Landmark = models.CharField(max_length=200,blank=True)
    Alternate_phone = models.CharField(max_length=10,blank=True)