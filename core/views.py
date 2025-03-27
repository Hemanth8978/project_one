from django.shortcuts import render
from .models import ProductVariants,Categories,Product
from django.views import View

# Create your views here.

class Home_view(View):
    def get(self,request):
        qs=ProductVariants.objects.all()
        categories=Categories.objects.filter(parent_category=None)
        context={
            'products':qs,
            'categories':categories
        }
        return render(request,'core/home.html',context)
# def fashion_view(request,category):

class CategoryProductsView(View):
    def get(sef,request,*arge,**kwargs):
        category=kwargs['category']
        category_obj=Categories.objects.get(name=category)
        items=Product.objects.filter(category_id=category_obj)
        qs=ProductVariants.objects.filter(product_id__in=items)
        context={
            'products':qs,
            'category':category
        }
        return render(request,'core/category_products.html',context)

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
        slug=kwargs['slug']
        product=ProductVariants.objects.get(slug=slug)
        context={
            'product':product
        }
        return render(request,'core/product_detail.html',context)

        

    

