from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from core.models import Product,ProductVariants
from authentication.models import CustomUser
from django.contrib.auth.models import User
from .models import Orderitem,Orders
from django.http import HttpResponse
# Create your views here.


class Addtocartview(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        username=request.user
        user=CustomUser.objects.get(username=username)
        product_slug=kwargs['slug']
        productVariant=ProductVariants.objects.get(slug=product_slug)
        product=Product.objects.create(product_id=productVariant.product_id.product_id)
        orderitem=Orderitem.objects.create(product_id=product,price=productVariant.sale_price,quantity=1)
        total=Orderitem.quantity * Orderitem.price
        Orders.objects.create(Order_item=orderitem,total=total,status='no placed',user_id=user)
        return HttpResponse('prduct added to cart successfully')
    
def sample():
    pass