from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.Register_View.as_view(),name='register'),
    path('login/',views.login_view.as_view(),name='login'),
    path('logout/',views.login_view.as_view(),name='logout'),
    path('identifyuser/',views.identifyUser.as_view(),name='identifyuser'),
    path('otpverification/<str:username>/',views.ValidateOTPV_view.as_view(),name='otp'),
    path('resetpassword/<str:username>/',views.setpassword_view.as_view(),name='setpass'),
    path('home/',views.Home_view.as_view(),name='home')
]