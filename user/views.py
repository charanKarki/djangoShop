from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

class signup(View):
    form = UserCreationForm()
    def get(self,request):
        return render(request,'signup.html',{'form':signup.form})
    
    def post(self,request):
        user = UserCreationForm(request.POST)
        if(user.is_valid()):
            user.save()
            user = authenticate(request,username=user.cleaned_data['username'],password=user.cleaned_data['password1'])
            login(request,user)
            return redirect('/')
        else:
            return render(request,'signup.html',{'form':signup.form})

