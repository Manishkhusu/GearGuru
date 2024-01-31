from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.views import View



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


def dashboard_view(request):
    user = request.user
    return render(request, 'base.html', {'user' : user})


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
        return redirect('cart')    
    else:  
        return render(request, "details.html", context)
   

def cart_view(request , cart_id):
    # Retrieve the product based on the provided product_id

    user = request.user
    cart_id = AddToCart.objects.get(id = cart_id)
    cart_items = AddToCart.objects.filter(user = user)


    context = {
        'cart_items' : cart_items,
    }

    if request.method == "POST":
        PurchasedProduct.objects.create(add_to_cart = cart_items )
    return render(request, 'cart.html', context)

    
    


class PurchasedProductsView(View):
    def get(request, cart_id):
        # Retrieve the product based on the provided product_id
        cart_items = AddToCart.objects.filter(id = cart_id).first()
        PurchasedProduct.objects.create(add_to_cart = cart_items)
        # cart_items.delete()
        return redirect('purchased')
    
def errornotfoundView(request):
    return render(request, 'errornotfound.html')




    



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



