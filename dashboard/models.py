from django.db import models

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
    
class AddToCart (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} added at {self.added_at}"
    
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
    


