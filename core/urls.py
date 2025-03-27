from django.urls import path
from . import views

urlpatterns=[
    path("",views.Home_view.as_view(),name='home'),
    path('category/<str:category>/',views.CategoryProductsView.as_view(),name='category'),
    path('product/<str:slug>/',views.ProductDetailView.as_view(),name='product')
]