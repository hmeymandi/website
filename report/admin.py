from django.contrib import admin
from .models import *

@admin.register(Reportmodel)
class Reportadmin(admin.ModelAdmin):
    field=['user','shift','user']
    list_display=['user','shift','date','category_to_str']


    def category_to_str(self,obj):
    
        return "".join([category.title for category in obj.categ.all()])

@admin.register(Informationmodel)
class Informationadmin(admin.ModelAdmin):
    fields=['title','slug','status','position']
    list_filter=(['status'])
    list_display=['title','slug','status','position']




   