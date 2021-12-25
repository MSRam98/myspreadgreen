from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.contrib.auth.models import Group
from django.http import request
from django.shortcuts import redirect, render
from .models import Customerdetail, Order,Product,Cart
from mygreen.forms import user_registration
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import restrict_login,allow_user

# Create your views here.
def home (request):
    return render(request,'mygreen/home.html')

@restrict_login
def Registration (request):
    form=user_registration()
    if request.method == 'POST':
        form=user_registration(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Customer')
            user.groups.add(group)
            customer=Customerdetail.objects.create(user=user,name=user.username,email=user.email)
            customer.save()
            messages.success(request,"Account Created Successfully")
            return redirect("login")
    
    regdict={'form':form}
    return render(request,'mygreen/registration.html',regdict)

@restrict_login
def Login (request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request.POST,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('shop')
        else:
            messages.info(request,"Enter correct username or password") 
    return render(request,'mygreen/login.html')

def services (request):
    return render(request,'mygreen/services.html')

@login_required(login_url='login')
def shop (request):
    customer = request.user.customerdetail
    userdict={'customer':customer,'mangotree':1,'lemontree':2,'amlatree':3,'neemtree':4,'nellitree':5,'peepaltree':6}
    return render(request,'mygreen/shop.html',userdict)

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def productview(request,pk):
    products=Product.objects.get(id=pk)
    productdict={'products':products}
    return render(request,'mygreen/productview.html',productdict)

@login_required(login_url='login')
def addcart(request,pk):
    user=request.user
    product=Product.objects.get(id=pk)
    name=user.username
    addingcart=Cart.objects.create(name=name,user=user,product=product)
    addingcart.save()
    return redirect('shop')

@login_required(login_url='login')
def cart(request):
    user=request.user
    name=user.username
    carts=Cart.objects.filter(name=name)
    cartdict={'carts':carts}
    return render(request,'mygreen/cart.html',cartdict)

@login_required(login_url='login')
def cartremove(request,pk):
    cartitem=Cart.objects.get(id=pk)
    cartitem.delete()
    return redirect('cart')
@login_required(login_url='login')
def buy(request,pk):
    if request.method == 'POST':
        user=request.user
        name=user.username
        product=Product.objects.get(id=pk)
        productname=product.productname
        housenumber=request.POST.get('housenumber')
        street=request.POST.get('street')
        city=request.POST.get('city')
        distric=request.POST.get('distric')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        comma=","
        paymentmode=request.POST.get('paymentmode')
        contactnumber=request.POST.get('contactnumber')
        address=housenumber+comma+street+comma+city+comma+distric+comma+state+comma+pincode
        orderobject=Order.objects.create(name=name,productname=productname,user=user,product=product,address=address,contactnumber=contactnumber,paymentmode=paymentmode)
        orderobject.save()
        return redirect('shop')

    return render(request,'mygreen/buy.html')

@login_required(login_url='login')
def orderhistor(request):
    user=request.user
    name=user.username
    orders=Order.objects.filter(name=name)
    orderdict={'orders':orders}
    return render(request,'mygreen/orderhistory.html',orderdict)

def customerprofile(request):
    customer=request.user.customerdetail
    customerdict={'customer':customer}
    return render(request,'mygreen/customerprofile.html',customerdict)

def editprofile(request):
    customer=request.user.customerdetail
    user=request.user
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contactnumber=request.POST.get('contactnumber')
        address=request.POST.get('address')
        profilepic=request.FILES.get('profilepic')
        customer.name=name
        customer.email=email
        customer.contactnumber=contactnumber
        customer.address=address
        if profilepic is not None:
            customer.profilepic=profilepic
        user.email=email
        customer.save()
        user.save()
        return redirect('customerprofile')
    mydict={'customer':customer}
    return render(request,'mygreen/editprofile.html',mydict)


@login_required(login_url='login')
def orderdetails(request,pk):
    order=Order.objects.get(id=pk)
    orderdict={'order':order}
    return render(request,'mygreen/orderdetails.html',orderdict)

@login_required(login_url='login')
def orderdelete(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()
    return redirect('orderhistory')

@login_required(login_url='login')    
@allow_user(allow_role=['Admin',])
def adminorderhistory(request):
    orders=Order.objects.all()
    orderdict={'orders':orders}
    return render(request,'mygreen/adminorderhistory.html',orderdict)

@login_required(login_url='login')    
@allow_user(allow_role=['Admin',])
def adminorderupdate(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        orderstatus=request.POST.get('orderstatus')
        if orderstatus is not None:
            order.orderstatus=orderstatus
            order.save()
            return redirect('adminorderhistory')
    orderdict={'order':order}
    return render(request,'mygreen/adminorderupdate.html',orderdict) 

