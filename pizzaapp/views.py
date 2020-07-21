from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.sessions.models import Session
from .decorators import admin_login_required,user_login_required
from django.contrib.auth.models import User
from .models import PizzaModel,CustomerModel,OrderModel
from .forms import PizzaModelForm
# Create your views here.
def adminlogin(request):
    return render(request,"pizzaapp/adminlogin.html")

#with session storing
def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = authenticate(username = username, password = password)

        #if user exsist
        if user is not None:
            #request.session.set_expiry(30)      #session will expire in 30 seconds
            request.session['user'] = user.username
            request.session['user_id'] = user.id

            #login(request,user)
            return redirect('adminhomepage')
        else:
            messages.error(request,'Please enter valid username and password')
            return redirect('adminloginpage')
    except(Exception):
        messages.error(request,'Please enter valid username and password')
        return redirect('adminloginpage')
    return render(request,'pizzaapp/adminlogin.html')

    #if user doesn't exsist
    # if user is None:
    #      messages.add_message(request,messages.ERROR,"Invalid Credentials")
    #      return redirect('adminloginpage')
@admin_login_required
def adminhomepageview(request):
    context = {'pizza' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context)

def adminlogoutview(request):
    logout(request)
    return redirect('adminloginpage')

def adminforgetpasswordview(request):
    return render(request,'pizzaapp/adminforgetpassword.html')

@admin_login_required
def addpizzaview(request):
    # pizzaname = request.POST['pizzaname']
    # desc = request.POST['desc']
    # p = request.POST['price']
    # price = float(p)
    # if (request,method == 'POST'):
    #     PizzaModel(pizzaname = pizzaname, desc = desc, price = price).save()
    # return redirect('adminhomepage')
    # return render(request,'addpizza.html')
    if (request.method == 'POST'):
        pizzaform = PizzaModelForm(request.POST)
        if (pizzaform.is_valid()):
            pizzaform.save()
        return redirect('adminhomepage')

    pizzaform = PizzaModelForm()
    return render(request, 'pizzaapp/addpizza.html', {'pizzaform': pizzaform})

@admin_login_required
def deletepizzaview(request, id):
    obj = PizzaModel.objects.get(pk=id)
    obj.delete()
    return redirect('adminhomepage')

@admin_login_required
def updatepizzaview(request, id):
    obj = PizzaModel.objects.get(pk=id)
    pizzaform = PizzaModelForm(instance=obj)
    if (request.method == 'POST'):
        pizzaform = PizzaModelForm(request.POST, instance=obj)
        if (pizzaform.is_valid()):
            pizzaform.save()
        return redirect('adminhomepage')
    pizzaform = PizzaModelForm(instance=obj)
    return render(request, 'pizzaapp/updatepizza.html', {'pizzaform': pizzaform, 'obj': obj})

def homepageview(request):
    return render(request, 'pizzaapp/homepage.html')

def signupuserview(request):
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    confirm_password =  request.POST['confirm_password']
    # if username already exists
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"User Already Exists!")
        return redirect('homepage')
    # if username doesnt exist already(everything is fine to create user)
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(lastobject)].id,email = email, phone = phone, confirm_password = confirm_password).save()
    messages.add_message(request,messages.ERROR,"User successfully Created!")
    return redirect('homepage')

def loginuserview(request):
    return render(request,"pizzaapp/loginuser.html")

#without session storing
def authenticateuser(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username,password = password)

	# user exists
	if user is not None:
		login(request,user)
		return redirect('userwelcomepage')

	# user doesnt exists
	if user is None:
		messages.add_message(request,messages.ERROR,"invalid credentials")
		return redirect('loginuserpage')

def welcomeuserview(request):
    if not request.user.is_authenticated:
        return redirect('loginuserpage')

    username = request.user.username
    context = {'username' : username,'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/userwelcome.html", context)

def userlogoutview(request):
    logout(request)
    return redirect('loginuserpage')

def placeorderview(request):
    if not request.user.is_authenticated:
        return redirect('loginuserpage')

    username = request.user.username
    phone = CustomerModel.objects.filter(userid = request.user.id)[0].phone
    address = request.POST['address']
    ordereditems = ""

    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        pizzaname = pizza.pizzaname
        desc = pizza.desc
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")


        if str(quantity)!="0" and str(quantity)!=" ":
            ordereditems = ordereditems + "Pizza Name: " + pizzaname  + "Pizza Description:" + desc + "Price: " + str(int(quantity)*float(price)) + "Quantity: " + quantity + "   "
            print(ordereditems)


    OrderModel(username = username, phone = phone, address = address, ordereditems = ordereditems).save()
    messages.add_message(request,messages.ERROR,"Order successfully Created")
    return redirect('userwelcomepage')


def userordersview(request):
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders': orders}
    return render(request,'pizzaapp/userorders.html',context)

def adminordersview(request):
    orders = OrderModel.objects.all()
    context =  {'orders':orders}
    return render(request,'pizzaapp/adminorders.html',context)

def acceptorderview(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "Accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
    
def declineorderview(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "Declied"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
