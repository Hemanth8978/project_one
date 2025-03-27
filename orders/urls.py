from django.urls import path
from . import views
urlpatterns=[
    path('addtocart/',views.Addtocartview.as_view(),name="addtocart")
]