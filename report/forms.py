from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from django.http import request
from .models import *
from .models import User
from django.contrib.auth import get_user_model as user_model



User=user_model()


class Reportform(forms.ModelForm):
    class Meta:
        model=Reportmodel

       
        fields=['subject','categ','slug','date','report','shift','user','acepet']
        
    
    