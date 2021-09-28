from django.urls import path
from . import views

app_name='rest'

urlpatterns = [

        path('create',views.Restcreate.as_view(),name='restform'),
        path('myrest',views.rest,name='myrest'),

        path('update/<int:pk>',views.Restupdate.as_view(),name='update'),


]