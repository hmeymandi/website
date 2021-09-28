from rest.models import Repmodel
from django.contrib import admin
from .models import Restmodel

# Register your models here.

@admin.register(Restmodel)
class Restadmin(admin.ModelAdmin):
    fields=['user','user1','type','accept','time1','time2','date','dateexit']
    list_filter=['accept']
    list_display=['user','user1','type','accept','time1','time2','date','dateexit']

@admin.register(Repmodel)
class Repadmin(admin.ModelAdmin):
    fields=['user','date','name','station','subj']
    list_filter=['station','subj']
    list_display=['user','date','name','station','subj']
    
