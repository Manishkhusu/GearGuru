from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *



def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            return(request, 'login.html', {'error' : 'invalid credentials'})
        
def user_signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = User(username = username)
        user.set_password(password)
        user.save()
        return redirect('login')
    
def logout_view(request):
    logout(request)  
    return redirect('login') 


def home_page(request):
    return render(request, 'home.html')

def product_page(request):
    products = Product.objects.all()
    return render(request, "product.html", {'products': products})

def detail_views(request, product_id):
    product = Product.objects.get(id = product_id)
    product_detail = Detail.objects.get(product = product)
    context = {
        'product' : product,
        'product_detail' : product_detail
        
    }
    # print(cart_items.quantity)
    if request.method == 'POST':
        # # Create or update the item in the cart
        cart_items = AddToCart.objects.filter(product = product_id).first()  
        cart_items.quantity += 1
        cart_items.save()
        return redirect('add_to_cart/{}'.format(product_id))    
    else:  
        return render(request, "details.html", context)
   

def add_to_cart_view(request, product_id):
    # Retrieve the product based on the provided product_id
    cart_items = AddToCart.objects.filter(product = product_id)

    context = {
        'cart_items' : cart_items,
    }

    return render(request, 'cart.html', context)
    
    



# def buy_now(request):
#     if request.method == 'POST':
#         form = BuynowForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')  # Redirect to a success page after successful submission
#     else:
#         form = BuynowForm()
#     return render(request, 'order.html', {'form': form})

# def success_page(request):
#     return render(request, 'success_page.html')



