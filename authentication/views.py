from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserForm,IdentifyUserForm,OTPform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.core.mail import send_mail
from .models import CustomUser
import random
import datetime
from django.utils import timezone
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here. 

def get_otp(username):
    obj=CustomUser.objects.get(username=username)
    otp=random.randint(1000,9999)
    otp_expiry=timezone.now()+datetime.timedelta(minutes=10)
    obj.otp=otp
    obj.otp_expiry=otp_expiry
    obj.save()
    print(otp_expiry)
    return otp,otp_expiry


class Register_View(View):
    def get(self,request,*args,**kwargs):
        context={
            'form':CustomUserForm()
        }
        return render(request,'authentication/register.html',context)
    def post(self,request,*args,**kwargs):
        fm=CustomUserForm(request.POST)
        if fm.is_valid():
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email']
            fm.save()
            send_mail(
                'Account Registration',
                f'Hi {first_name} {last_name}\n Welcome to Ecommerce application your account has been created',
                'hemanthahemanthraj464@gmail.com',
                [email],
                fail_silently=False

            )
            messages.success(request,'account created successfully')
            return redirect('login')
        messages.error(request,'somthing wrong check once')
        return render(request,'authentication/register.html',{'form':fm})
    
class login_view(View):
    def get(self,request):
        context={
            'form':AuthenticationForm()
        }
        return render(request,'authentication/login.html',context)
    def post(self,request):
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request,user)
                    messages.success(request,'logined successfully')
                    # return render(request,'authentication/home.html')
                    return redirect('home')
        # return HttpResponse('invalid credentials')
        messages.error(request,'invalid username or password')
        return redirect('login')
    
class logout_view(View):
    def get(self,request):
        logout(request)
        return redirect('logout')
    
class identifyUser(View):
    def get(self,request):
        fm=IdentifyUserForm()
        context={
            'form':fm
        }
        return render(request,'authentication/identify.html',context)
    def post(self,request):
        fm=IdentifyUserForm(data=request.POST)
        if fm.is_valid():
            username_or_email=fm.cleaned_data['username_or_email']
            qs=CustomUser.objects.filter(Q(username=username_or_email)|Q(email=username_or_email))
            if qs.exists():
                user=qs[0]
                email=user.email
                otp,otp_expiry=get_otp(user.username)
                msg = f'Dera {user.first_name} {user.last_name}here your OTP(one time password) to reset the password \n {otp}\n this validate untill {otp_expiry}\n Dont share OTP with any one'
                send_mail(
                'OTP Verification',
                msg,
                'hemanthahemanthraj464@gmail.com',
                [email],
                fail_silently=False
                )
                context={
                    'user':user
                }
                return render(request,'authentication/otp.html',context)
            # user=None
            # context={
            #     'user':user
            # }
            # return render(request,'authentication/otp.html',context)
            messages.error(request,'user not found')
            return redirect('identifyuser')
        
class Home_view(View):
    @method_decorator(login_required)
    def get(self,request):
        return render(request,'core/home.html')
        
class ValidateOTPV_view(View):
    def get(self,request,*args,**kwargs):
        user=CustomUser.objects.get(username=kwargs['username'])
        context={
            'form':OTPform()
        }
        return render(request,'authentication/otpverification.html',context)
    def post(self,request,*args,**kwargs):
        username=kwargs['username']
        user=CustomUser.objects.get(username=kwargs['username'])
        fm=OTPform(request.POST)
        if fm.is_valid():
            otp=fm.cleaned_data['enter_otp']
            if user.otp_expiry>=timezone.now():
                if otp==user.otp:
                    url=f"/authentication/resetpassword/{username}/"
                    return redirect(url)
                else:
                    messages.error(request,'OTP is not same')
                    return redirect(f"/authentication/otpverification/{user.username}")
                    # return HttpResponse('otp is not same')
            # return HttpResponse('otp expired')
            messages.error(request,'OTP was expired so please reset agian')
            return redirect('identifyuser')

class setpassword_view(View):
    def get(self,request,*args,**kwargs):
        user=CustomUser.objects.get(username=kwargs['username'])
        fm=SetPasswordForm(user=user)
        context={
            'form':fm
        }
        
        return render(request,'authentication/setpassword.html',context)
    
    def post(self,request,*args,**kwargs):
        user=CustomUser.objects.get(username=kwargs['username'])
        # user=kwargs['username']
        email=user.email
        fm=SetPasswordForm(user=user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'password reset successfully')
            send_mail(
                'Password Reset completed',
                f'Dear {user.first_name} {user.last_name} Your password reset completed successfully',
                'hemanthahemanthraj464@gmail.com',
                [email],
                fail_silently=False
            )
            return redirect('login')
        messages.error(request,'password reset faild')
        return redirect('identifyuser')
        # return HttpResponse('reset fiald')


        