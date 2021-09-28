from django.contrib.admin.widgets import AdminRadioSelect
from django.db.models import manager
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




# Create your views here.


class Restcreate(LoginRequiredMixin,Jalali2date,FormValid,FieldMixin,CreateView):
    model=Restmodel

    template_name='rest.html'
    
    #form_class=Restform
    def get_success_url(self):
        return reverse('rest:myrest')
    
    



class Restupdate(AccsesMixin,FieldMixin,UpdateView):
    model=Restmodel
   
    template_name='rest.html'

    def get_success_url(self):
        return reverse('rest:myrest')

@login_required
def rest(request):

    if request.user.is_admin or request.user.is_nazer\
         or request.user.is_manager:
                
        form=Restmodel.objects.all().order_by('-time1')
        return render(request,'resthome.html',{'form':form})

    else:

        form=Restmodel.objects.filter(user1=request.user.id)
        return render(request,'resthome.html',{'form':form})