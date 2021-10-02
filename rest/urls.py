from django.urls import path
from . import views

app_name='rest'

urlpatterns = [

        path('create',views.Restcreate.as_view(),name='restform'),
        path('myrest',views.rest,name='myrest'),
        
        path('repcreate',views.RepCreate.as_view(),name='repcreate'),
        path('repupdate/<int:pk>',views.Repupdate.as_view(),name='repupdate'),

        path('rephome',views.rephome,name='rephome'),
        path('update/<int:pk>',views.Restupdate.as_view(),name='update'),



]