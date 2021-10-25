from django.contrib import admin
from .models import *

@admin.register(Reportmodel)
class Reportadmin(admin.ModelAdmin):
    
    field=['user','shift','subject']
    list_filter=['date','user']
    list_display=['user','shift','date','category_to_str']
    prepopulated_fields={'slug':('subject',)}   

    def category_to_str(self,obj):
    
        return "".join([category.title for category in obj.categ.all()])
    def __str__(self):
    
        return "{} {} {} {} ".format(self.subject,self.date,self.user,self.shift)

@admin.register(Informationmodel)
class Informationadmin(admin.ModelAdmin):
    fields=['title','slug','status','position']
    list_filter=(['status'])
    list_display=['title','slug','status','position']

@admin.register(StationModel)
class StationModeladmin(admin.ModelAdmin):
    fields=['mastername','titel','position','slug','status']
    list_fields=['mastername']
    list_display=['mastername','slug','status']

@admin.register(DeviceModel)
class devicemodeladmin(admin.ModelAdmin):
    fields=['device_name','position','slug','status','name']
    list_fields=['device_name']
    list_display=['device_name','slug','status','name']




   