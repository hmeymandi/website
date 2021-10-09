from django.urls import path,include
from . import views
from .views import *

app_name='account'
urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('profile',Profile.as_view(),name='profile'),
    path('password_change/',views.PasswordChange,name='password_change'),
    path('rest/',views.RestPassword.as_view(),name='rest'),
    path('rest/done/',views.DonePassword.as_view(),name='done'),
    path('confrim/<uidb64>/<token>/',views.Passwordrestconfig.as_view(),name='Passwordrestconfig'),
    path('confrim/done',views.Complate.as_view(),name='comlate'),

]