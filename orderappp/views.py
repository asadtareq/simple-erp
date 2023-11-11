from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import product, signuptbl
from .forms import NameForm

#add new product
@login_required()
def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        prd = product(
          name = name,
          quantity = quantity,
          price = price,
          amount = amount
        )
        prd.save()
        messages.success(request,"Success")
        return redirect ('order')
        
#edit product
@login_required()
def edit_product(request, id):
    prd = product.objects.filter(id = id)
    return render(request,'edit-order.html',{'ep':prd})

#update product
@login_required()
def update_product(request, id):
    if request.method == "POST":
        name = request.POST.get('uname')
        quantity = request.POST.get('uquantity')
        price = request.POST.get('uprice')
        uprd = product(
          name = name,
          quantity = quantity,
          price = price,
          id = id
        )
        uprd.save()
        messages.success(request,"Update Success")
        return redirect ('order')

#delete product
@login_required()
def delete_product(request, id):
    prd = product.objects.filter(id = id)
    prd.delete()
    return redirect('order')




#show profile
@login_required()
def showprofile(request):
    profile = signuptbl.objects.all()
    return render(request, "profile.html",{'showp':profile})


#signup form view
def signupviewfunc(request):
    #show_notice=notice.objects.all()
    return render(request, "signup.html")


#User Registration
def user_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        userreg = signuptbl(
          name = name,
          email = email,
          password = password
        )
        userreg.save()
        messages.success(request,"Success")
        return render(request, "signup.html")
    else:
        messages.success(request, "Failed")
 



#- login function
def index(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #request.session['username'] = username
            messages.success(request, "Login Success")
            return redirect('dashboard')
        else:
            messages.success(request, "Login Fails")
            return redirect('index')
    else:
        return render(request, 'index.html')
    
#dashboard page
@login_required()
def dashboardfunc(request):
    return render(request, "dashboard.html")

#Order page
@login_required()
def orderfunc(request):
    show_product=product.objects.all()
    #qty = product.objects.raw("SELECT quantity FROM product")
    return render(request, "order.html",{'sp': show_product})

    
#logout function
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logout... Try again")
    return redirect('index')


#view product
@login_required()
def product_view(request):
    show_product=product.objects.all()
    return render(request, "index.html",{'sp': show_product})



#register/create new user
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Success")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html', {'form':form})