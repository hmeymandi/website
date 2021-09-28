from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import request
from django.forms import forms
from django.shortcuts import redirect






class FieldMixin():

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_admin:
             self.fields=['subject','report','date','user','shift','slug','acepet']
        elif self.request.user.is_authe:
             self.fields=['subject','report','date','user','shift','slug']
        
        
        return super().dispatch(request, *args, **kwargs)
class FormValidMixin():
     def form_valid(self,form):
          if self.request.user.is_admin:
               form.save()
        
          else:
               self.obj=form.save(commit=False)
               self.obj.user=self.request.user
               self.obj.acepet='تایید نشده'
          return super().form_valid(form)



def unauthanticate(my_func):
    def warper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('net:home')
        else:
            return my_func(request,*args,**kwargs)
    return warper_func


def mix(my_func):
    def warper_func(request,*args,**kwrgs):
        if request.user.is_admin:
            fields=['subject','report','date','user','shift','slug','acepet']
            return 
        elif request.user.is_authe:
            fields=['subject','report','date','user','shift','slug']
            return my_func(request,*args,**kwrgs)
    return warper_func