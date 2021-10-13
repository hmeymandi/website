from django.contrib.admin.widgets import AdminRadioSelect
from django.db.models import manager
from accounts.models import User as user3


from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from jalali_date.fields import JalaliDateField, JalaliDateTimeField
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView
from django import forms
from .mixin import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.contrib.auth.models import AbstractBaseUser, UserManager 
from accounts.models import User

User=user_model()



# Create your views here.


class Restcreate(LoginRequiredMixin,Jalali2date,FormValid,FieldMixin,CreateView):
    model=Restmodel
    
    
    template_name='rest.html'
    
    
    def get_success_url(self):
        return reverse('rest:myrest')

    def get_form(self,form_class=None):
        
        form=super().get_form(form_class)
        if self.request.user.is_admin or self.request.user.is_nazer:

            user2=User.object.all()
            form.fields['user'].queryset =user2
            return form
        else:
            user2=User.object.filter(is_admin=False,is_nazer=False)
            form.fields['user'].queryset =user2
        
        return form
        
      
       
        

           

        
        
        
        

class RepCreate(LoginRequiredMixin,FormRepValid,FieldRepMixin,CreateView):
    model=Repmodel
    #fields='__all__'
    template_name='rep.html'
    
    def get_form(self,form_class=None):
        form=super().get_form(form_class)

        form.fields['date'].disabled=True
        return form
        
    
    def get_success_url(self):
        return reverse('rest:rephome')

class Repupdate(AccsesrepMixin,FieldRepMixin,UpdateView):
    model=Repmodel
    template_name="rep.html"

    def get_form(self,form_class=None):
        form=super().get_form(form_class)

        form.fields['date'].disabled=True
        return form
        

    def get_success_url(self):
        return reverse('rest:rephome')

class Restupdate(AccsesMixin,FieldMixin,UpdateView):
    model=Restmodel
   
    template_name='rest.html'

    def get_success_url(self):
        return reverse('rest:myrest')
@login_required
def rephome(request):
    form=Repmodel.objects.all().order_by('-date')
    return render (request,'rephome.html',{'form':form})

@login_required
def rest(request):

    if request.user.is_admin or request.user.is_nazer\
         or request.user.is_manager:
                
        form=Restmodel.objects.all().order_by('-time1')
        return render(request,'resthome.html',{'form':form})

    else:

        form=Restmodel.objects.filter(user1=request.user.id)
        return render(request,'resthome.html',{'form':form})