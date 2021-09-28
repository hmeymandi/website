from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    form=UserchangeForm
    add_form=UserCreationForm

    list_display=('idcart','first_name','last_name','phone','shift','date')
    list_filter=('idcart','is_active')
    fieldsets=((User, {'fields': ('idcart','first_name','last_name','shift', 'password','date')}),
    ('وضیعت کاربر',{'fields':('is_admin','is_nazer','is_active','is_authe','is_manager')}),
    #('permasion',{'fields':('is_active',)}),
    #('permasion',{'fields':('is_authe',)}),
    #('permasion',{'fields':('is_manager',)}),
    #('Personal info',{'fields':('is_nazer',)})
    )
    add_fieldsets = (
        (None, {
            
            'fields': ( 'first_name', 'last_name','idcart','email','phone','address','date','shift', 'password1','password2'),
        }),
    )
    search_fields=('idcart', )
    ordering=('idcart',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)    
admin.site.unregister(Group)
