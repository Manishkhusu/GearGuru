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
    product = get_object_or_404(Product, id=product_id)
    return render(request, "details.html", {'product': product})
   

def add_to_cart_view(request, product_id):
    # Retrieve the product based on the provided product_id

    product = get_object_or_404(Product, pk=product_id)

    # Create or update the item in the cart
    if AddToCart.objects.filter(product=product).exists():
        cart_item = AddToCart.objects.get(product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = AddToCart.objects.create(product=product, quantity=1)

    # Redirect the user to the cart page
    return redirect('add_to_cart/{}'.format(product.id))

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



