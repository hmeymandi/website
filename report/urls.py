from django.urls import path
from .views import *

app_name='net'
urlpatterns = [

        path('listreport',listreport,name='listreport'),
        path('detailreport/<slug:slug>',Reportdeatail.as_view(),name='detail'),
        path('reportform/create',ReportCreate.as_view(),name='reportform'),
        path('myreport',myreport,name='myreport'),
        path('home',home,name='home'),
        path('reportform/update/<int:pk>',Reportupdate.as_view(),name='reportupdate'),

]