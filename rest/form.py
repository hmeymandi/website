from django.forms import fields
from .models import Restmodel
from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime




class Restform(forms.Form):
  
        time1=forms.DateTimeField(widget=AdminJalaliDateWidget)

    