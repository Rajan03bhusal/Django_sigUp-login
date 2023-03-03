from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .form import *
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request,'core/home.html')

class SingupView(View):
    def get(self,request):
         fm=SignUpForm()
         return render(request,'core/Sigup.html',{'form':fm})
    

    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Successfully!!")
            return redirect('/Sigup')
        else:
            return render(request,'core/Sigup.html',{'form':fm})

        
    
class MyloginView(View):
    def get(self,request):
        fm= MyLoginForm()
        return render(request,'core/login.html',{'form':fm})
    
    def post(self,request):
        fm=MyLoginForm(request,data=request.POST)
        if fm.is_valid():
           Username=fm.cleaned_data['username']
           password=fm.cleaned_data['password']
           user= authenticate(request, username=Username,password=password)
           if user is not None:
               login(request, user)
               return redirect ('/')
           else:
               return render(request, 'core/login.html',{'form':fm})

         

        else:
            return render(request,'core/login.html',{'form':fm})

        
    
    


        
   