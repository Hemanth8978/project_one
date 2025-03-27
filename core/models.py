from django.db import models
from authentication.models import CustomUser

# Create your models here.

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='category_image/',null=True,blank=True)
    parent_category=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    # price = models.FloatField()
    # stock = models.IntegerField()  
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=200)
    createdat = models.DateField(auto_now_add=True)
    brand=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


class ProductVariants(models.Model):
    variant_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    attribute = models.CharField(max_length=200,null=True,blank=True)
    value = models.IntegerField(null=True,blank=True)
    extra_price = models.FloatField(null=True,blank=True)
    image1 = models.ImageField(upload_to='products/', blank=True,null=True)
    image2 = models.ImageField(upload_to='products/', blank=True,null=True)
    image3 = models.ImageField(upload_to='products/', blank=True,null=True)
    stock=models.IntegerField(null=True,blank=True)
    original_price=models.FloatField(null=True,blank=True)
    sale_price=models.FloatField(null=True,blank=True)
    discount_per=models.IntegerField(null=True,blank=True)
    color=models.CharField(max_length=100,null=True,blank=True)
    slug=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return f"{self.product_id}-{self.color}"
    def save(self,*args,**kwargs):
        self.slug=str(self.product_id.name).replace(" ","-")
        super().save(*args,**kwargs)
class Product_Attributes(models.Model):
    attribute_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute=models.CharField(max_length=200)
    value=models.IntegerField()

class Reviews(models.Model):
    reviews_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.FloatField()
    review_text=models.TextField()
    createdat=models.DateField(auto_now_add=True)

class Dgital_product(models.Model):
    digital_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    file_url=models.TextField(max_length=200)
  
class ProductSizeOption(models.Model):
    size_id=models.AutoField(primary_key=True)
    product_variant=models.ForeignKey(ProductVariants,on_delete=models.CASCADE)
    size_category=models.CharField(max_length=200)
    size_name=models.CharField(max_length=200)
    sotck_in_qnt=models.IntegerField()


