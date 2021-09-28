from django import forms
from django.db.models import fields
from django.forms.forms import Form
from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UsercreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['first_name','last_name','idcart','phone','email','address','shift','date','password']

    def clean_password2(self):
        data=self.cleaned_data
        if data['password2'] and data['password1'] and data['password2'] !=data['password1']:
            raise forms.ValidationError('plz check password')
        return data['password2']


    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user    

class UserchangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField

    class Meta:
        model=User
        fields=['first_name','last_name','idcart','phone','email','address','shift','date','password']

    def clean_password(self):
        return self.initial['password']

class Userloginform(forms.Form):
    idcart=forms.CharField()
    password=forms.CharField(label='رمز عبور',widget=forms.PasswordInput)


class Profileforms(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(Profileforms,self).__init__(*args,**kwargs)
        if not user.is_admin:
            self.fields['idcart'].disabled=True
            self.fields['phone'].disabled=True
            self.fields['shift'].disabled=True
            self.fields['date'].disabled=True
            self.fields['is_nazer'].disabled=True
            self.fields['is_authe'].disabled=True
            self.fields['is_manager'].disabled=True
            self.fields['is_active'].disabled=True

    class Meta:
        model=User
        fields='__all__'

