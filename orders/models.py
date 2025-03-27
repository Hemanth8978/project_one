from django.db import models
from authentication.models import CustomUser
from core.models import Product
# Create your models here.
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total=models.IntegerField()
    status=models.CharField(max_length=200)
    createdat=models.DateField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
    order_item=models.ForeignKey('Orderitem',on_delete=models.CASCADE)
    

class Orderitem(models.Model):
    order_item_id=models.AutoField(primary_key=True)
    # order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    ordered=models.BooleanField(default=False)


class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount=models.FloatField()
    status=models.CharField(max_length=200)
    createdat=models.DateField(auto_now_add=True)

class Shipping(models.Model):
    shipping_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    tracking_no=models.IntegerField()
    status=models.CharField(max_length=200)