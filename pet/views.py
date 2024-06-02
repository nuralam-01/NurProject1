from email import message
from django.shortcuts import render
#from django.http import HttpResponseRedirect
from pet.models import Contact, AddProduct,Users
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import redirect
import json
from pet.form import newProduct

# Create your views here.
def about (request):
    return render (request,'about.html')
#views
def blog (request):
    return render (request,'blog.html')
#views
def contact (request):
    if request.method == "POST":
        myobject = Contact()
        myobject.Your_name= request.POST.get("name")
        myobject.Email= request.POST.get("email")
        myobject.Subject= request.POST.get("subject")
        myobject.Message= request.POST.get("message")
        myobject.save()
        return redirect(index)
    else:
        print("404 NOT FOUND")
        return render (request,'contact.html')

#views
def index (request):
    return render (request,'index.html')

#views
def showproduct (request):
    pro = AddProduct.objects.all()
    proDict = {'p':pro} 
    return render (request,'product.html',context=proDict)
#views
def random (request):
    return render (request,'random.html')
#views
def service (request):
    return render (request,'service.html')
#views
def team (request):
    return render (request,'team.html')
#views
def testimonial (request):
    return render (request,'testimonial.html')
#views
def ProductAdd (request):
    alldata =AddProduct.objects.all()
    p1 = newProduct()
    if request.method == 'POST':
        p1 = newProduct(request.POST,request.FILES or None)
        if p1.is_valid():
            p1.save()
            return redirect(ProductAdd)
    else:
        print("404 ERROR")
    return render (request,'addproduct.html',{'newform':p1, 'data':alldata})
#views
def deleteData(request,PK):
    DeleteData=AddProduct.objects.get(Pid=PK)
    DeleteData.delete()
    return redirect(ProductAdd)

def updateData(request, PK=0):
    prod = AddProduct.objects.get(Pid = PK)
    alldata =AddProduct.objects.all()
    p1 = newProduct(request.POST or None, request.FILES or None, instance=prod)
    if p1.is_valid():
        AddProduct.objects.filter(Pid=PK).update(Pid = prod.Pid)
        p1.save()
        return redirect(ProductAdd)
    else:
        print("error")
        
    return render(request, 'updateproduct.html',{'newform':p1, 'data':alldata})

#For Sign up's register part
def  SignUp(request):
    if request.method=='POST':
        name1=request.POST.get('username')
        email1=request.POST.get('email')
        password1=request.POST.get('pswd')
        cpassword1=request.POST.get('cpswd')
        user=Users.objects.filter(Email=email1)#users already exits or not
        if user:
            message='user already exist'
            return render(request,'about.html',{'msg:message'})
        else:
           if password1==cpassword1:
                newuser=Users.objects.create(Name=name1,Email=email1,Password=make_password(password1))
                message='user register successfully'
                return redirect(Login)
           else:
               message='password are not matching'
               return render(request,'SignUp.html',{'msg':message})
           #Subject='Welcome to PET SHOP'
        #send_mail(Subject,'Thank you for visiting our website',settings.EMAIL_HOST_USER,[email1])
    else:
        print("Error in data Submission")
    return render(request, "Signup.html")

#For Login
def Login(request):
    if request.method=='POST':
        email1=request.POST.get('email')
        password1=request.POST.get('pswd')
        # print(password1)
        #check with database
        user=Users.objects.get(Email=email1)
        #admin=adminData.objects.get(Email=email1)
        #print(user.Password)
        if user:
            #print(check_password(password1,user.Password))
            #print(user.Password)
            if check_password(password1,user.Password):
                request.session['name']=user.Name
                request.session['email']=user.Email
                return render(request,"index.html")
            else:
                message="password does not match"
                return render(request,"SignUp.html",{'msg':message})
        else:
            message="user does not exits"
            return render(request,"SignUp.html",{'msg':message})
    else:
        print("Error in data submission")
        return render(request,'Login.html')
    
#for addCart
def addcart(request,pid=101):
    product = AddProduct.objects.get(Pid=pid)
    cart= request.COOKIES.get('cart')
    if cart:
        cart = json.loads(cart)
    else:
        cart = {}
        cart[pid] = {
        'id': product.Pid,
        'name': product.Pname,
        'price': product.sale,
        } 
    
    return redirect('pro')

#For viewcart
def viewCart(request):
    return render(request,'cart.html')


        
            
        
        
        
               
        
        
    
    
