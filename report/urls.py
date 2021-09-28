from django.urls import path
from . import views

app_name='net'
urlpatterns = [

        path('listreport',views.listreport,name='listreport'),
        path('detailreport/<slug:slug>/<int:pk>',views.detailreport,name='detailreport'),
        path('reportform/create',views.ReportCreate.as_view(),name='reportform'),
        path('myreport',views.myreport,name='myreport'),
        path('home',views.home,name='home'),
        path('reportform/update/<int:pk>',views.Reportupdate.as_view(),name='reportupdate'),

]