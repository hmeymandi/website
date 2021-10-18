from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import HttpResponse
from django.http import request
from django.forms import forms
from report.models import *
from django.shortcuts import redirect
from django.db.models.signals import m2m_changed
from django.forms.widgets import PasswordInput, TimeInput
from django.forms import *



class FieldMixin():

    def dispatch(self, request, *args, **kwargs):
          
          if self.request.user.is_admin :
               
               self.fields=['subject','categ','slug','date','report','shift','user','acepet','numbercmms','device']
          elif self.request.user.is_authe or self.request.user.is_nazer or self.request.user.is_manager:

               self.fields=['subject','date','report','shift','acepet','numbercmms','device']
          elif self.request.user.is_active:
               self.fields=['subject','slug','date','report','shift','numbercmms','device']
               

        
        
          return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
     def form_valid(self,form):
          if self.request.user.is_admin:
               form.save()
        
          else:
               a=(Informationmodel.objects.get(position=2))
               
               #b=StationModel.objects.get(position=1)   
                                                                                                                                  
         
               
               form.instance.user=self.request.user
               self.obj=form.save()                                         
               if not self.obj.acepet in ['تایید سر شیفت','تایید نشده','تایید نهایی']:
                    self.obj.acepet='تایید نشده'                                
               self.obj.categ.set([a])                                 
                           
              
          return super().form_valid(form)


class FieldUpdateMixin():
    
    def dispatch(self, request,pk, *args, **kwargs):

          update=Reportmodel.objects.get(pk=pk)

          
          if update.user==request.user or request.user.is_admin \
           or request.user.is_authe or request.user.is_nazer or request.user.is_manager:
               
           

               return super().dispatch(request,*args,**kwargs)

          else:                   
               raise Http404('شما دسترسی به این بخش ندارید')
               
              
