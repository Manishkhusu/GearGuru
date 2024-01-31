from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)  

    def __str__(self):
        return self.name
    
class Detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=10000)

    def __str__(self):
        return self.product.name
    
class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self) -> str:
        return self.product.name

class PurchasedProduct(models.Model):
    add_to_cart = models.ForeignKey(AddToCart, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.add_to_cart.product.name

    @property
    def user(self):
        return self.add_to_cart.user

    @property
    def product(self):
        return self.add_to_cart.product

    @property
    def quantity(self):
        return self.add_to_cart.quantity

    @property
    def total_price(self):
        return self.add_to_cart.total_price

    
# class Buynow (models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     buyer_name = models.CharField(max_length=255)
#     buyer_email = models.EmailField()
#     shipping_address = models.TextField()
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order for {self.product.name} by {self.buyer_name}"
    


