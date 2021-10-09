from django.contrib.messages.api import success
from django.http import request
from django.shortcuts import render,redirect, resolve_url
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login as auth_login,logout as django_logout
from django.contrib import messages
from report.decorators import unauthanticate
from django.views.generic import CreateView,UpdateView

from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth import views as authviews



class RestPassword(authviews.PasswordResetView):
    template_name='restpasword.html'
    success_url=reverse_lazy('account:done')
    email_template_name='link.html'

class DonePassword(authviews.PasswordResetDoneView):
    template_name='donepassword.html'

class Passwordrestconfig(authviews.PasswordResetConfirmView):
    template_name='passwordrestconfig.html'
    success_url=reverse_lazy('account:comlate')

class Complate(authviews.PasswordResetCompleteView):
    template_name='complate.html'



@unauthanticate
def login(request):
    #if request.user.is_authenticated:
        #return redirect("account:home")

    
    #else:
        #form=Userloginform()
        if request.method=='POST':
            form=Userloginform(request.POST) 
            if form.is_valid():
                data=form.cleaned_data
                user=authenticate(request,idcart=data['idcart'],password=data['password'])
                if user is not None:
                    auth_login(request, user)
                    messages.success(request,'با موفقیت وارد شدید',extra_tags='success')
                    return redirect('net:listreport')
                else:
                    messages.success(request,'نام کاربری و پسورد شما اشتباه است',extra_tags='danger')

            
        else:
            form=Userloginform()
        
        return render(request,'login.html',{'form':form})




def logout(request):
    django_logout(request)
    messages.success(request,'با موفقیت خارج شدید',extra_tags='warning')
    return redirect('account:login')

class Profile(LoginRequiredMixin,UpdateView):
    model=User
    template_name='profile.html'
    form_class=Profileforms
    def get_object(self):
        return User.object.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs= super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user
         } )
                

        return kwargs



def PasswordChange(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'رمز عبور با موفیقت تغییر یافت','success')
            return redirect('account:profile')
        else:
            messages.error(request,'پسورد انتخابی صحیح نمی باشد','danger')
            redirect('account:password_change')

    else:

        form=PasswordChangeForm(request.user)

    return render(request,'pswchange.html',{'form':form})

    