from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Categories)
class Categoriesadmin(admin.ModelAdmin):
    list_display=['category_id','name','category_image','parent_category']

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display=['product_id','name','description','category_id','product_type','createdat','brand']

@admin.register(ProductCategory)
class ProductCategoryadmin(admin.ModelAdmin):
    list_display=['product_id','category_id']

@admin.register(ProductVariants)
class Prdouctvariantsadmin(admin.ModelAdmin):
    list_display=['variant_id','product','value','extra_price','image1','image2','image2','original_price','sale_price','discount_per','color']

@admin.register(Product_Attributes)
class Product_attributesadmin(admin.ModelAdmin):
    list_display=['attribute_id','product_id','value','attribute']

@admin.register(Reviews)
class Reviewsadmin(admin.ModelAdmin):
    list_display=['reviews_id','user_id','product_id','rating','review_text','createdat']
   
@admin.register(Dgital_product)
class Digitalproductadmin(admin.ModelAdmin):
    list_display=['digital_id','product_id','file_url']

@admin.register(ProductSizeOption)
class Productsizeoptionadmin(admin.ModelAdmin):
    list_display=['size_id','product_variant','size_category','size_name','sotck_in_qnt']