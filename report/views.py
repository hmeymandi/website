
from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from accounts.mixin import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.core.paginator import Paginator
from django.views.generic import CreateView,UpdateView,DetailView
from .decorators import mix, unauthanticate
from django.contrib.auth.decorators import login_required
from .forms import Reportform
from .forms import Informationmodel
from django.forms import *
#
@login_required
def listreport(request,):
    #if request.user is authenticate:
        
    #print(request.user.is_authe)
        report=Reportmodel.objects.filter(categ=2).order_by('-date')
        paginator=Paginator(report,10)   
        pagenum=request.GET.get('page')
        page_obj=paginator.get_page(pagenum)
        context={'report':page_obj}
    

        return render(request,'listreport.html',context)





#def detailreport(request,slug):
    
 #   form=Reportmodel.objects.get(slug=slug)
    
  #  return render(request,'deatil.html',{'form':form})
@login_required
def myreport(request):
    
    if request.user.is_admin or request.user.is_authe or request.user.is_nazer:
        myreport=Reportmodel.objects.all().order_by('-date')
        
        contax={'myreport':myreport}
        return render(request,'myreport.html',contax)

    else:
        myreport=Reportmodel.objects.filter(user=request.user.id)
        return render(request,'myreport.html',{'myreport':myreport})

def home(request):
    
    context={'categ':Reportmodel.objects.filter(categ=1).order_by('-date')}


    return render(request,'home.html',context)

    
class Reportdeatail(DetailView):
    template_name='detailreport.html'
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Reportmodel.objects.all(),slug=slug)

class ReportCreate(LoginRequiredMixin,FormValidMixin,FieldMixin,CreateView):
    model=Reportmodel
   #fields=['subject','categ','slug','date','report','shift','user','acepet']
    template_name='reportform.html'
    
    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        
        form.fields['date'].disabled=True
        
        return form    


class Reportupdate(FieldUpdateMixin,FieldMixin,UpdateView):
    model=Reportmodel
   
    template_name='reportform.html'
