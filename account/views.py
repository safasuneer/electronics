from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView,TemplateView,ListView
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from customer.models import shops

# Create your views here.
class Ehomeview(FormView):
    template_name="home.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            print(user)
            if user:
                login(request,user)
                return redirect("cus")
            else:
                messages.error(request,"Sigh in failed!!")
                return redirect('ehome')
        return render(request,"ehome.html",{"form":form_data})
        
   
class UserRegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,"Registration Successfull!!")
        return super().form_valid(form)
    


class CustomerView(TemplateView):
    template_name="cust_home.html"    

class AboutView(View):
    def get(self,request):
        return render(request,'about.html')
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')
class HelpView(View):
    def get(self,request):
        return render(request,'help.html')

class PricingView(View):
    def get(self,request):
        return render(request,'pricing.html')
class ServiceView(View):
    def get(self,request):
        return render(request,'service.html')
class TeamView(View):
    def get(self,request):
        return render(request,'team.html')
    
class ServiceView(ListView):
    template_name="team.html"
    queryset=shops.objects.all()
    context_object_name='ser'

class PaymentView(View):
    def get(self,request):
        return render(request,'payment.html')
    


    
    

   
    
