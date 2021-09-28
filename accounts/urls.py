from django.urls import path,include
from . import views
from .views import *

app_name='account'
urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('profile',Profile.as_view(),name='profile'),
]