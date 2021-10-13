from datetime import timedelta
from django.db import models
from report.models import Reportmodel,StationModel,DeviceModel
from django.contrib.auth import get_user_model as user_model
from django.db.models.aggregates import Avg
from django.db.models.fields import BLANK_CHOICE_DASH
from django.http import request
from jdatetime import datetime,date
import jdatetime
from jdatetime.jalali import JalaliToGregorian
from accounts.models import User
from django.utils import timezone
from django.db.models import F
from django.db.models.deletion import CASCADE
from jalali_date import datetime2jalali,date2jalali
from django_jalali.db import models as jmodels




User=user_model()


class Restmodel(models.Model):
    class Meta:
        verbose_name='مرحضی'
        verbose_name_plural='مرحضی'

    type_status=(('ساعتی','ساعتی'),('روزانه','روزانه'))
    accept_status=(('در دست بررسی','در دست بررسی'),
    ('تایید سرپرست','تایید سرپرست'),
    ('تایید ناظر','تایید ناظر'),
    ('تایید نشده','تایید نشده'))


    
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name='نام جایگزین')
    user1=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='user',verbose_name='نام کاربری')
    date=jmodels.jDateField(verbose_name='تاریخ ثبت')
    time1=models.TimeField(null=True,verbose_name='شروع مرخصی')
    time2=models.TimeField(null=True,verbose_name='پایان مرخصی')
    dateexit=jmodels.jDateField(verbose_name='تاریخ ورود')
    type=models.CharField(max_length=20,default='h',choices=type_status,verbose_name='نوع مرخصی')
    accept=models.CharField(default='در دست بررسی',max_length=30,choices=accept_status,verbose_name='وضیعت')
    
    




    def __str__(self):
        
        return '{} {} {}'.format(self.user,self.user1,self.type)

    

    def persian_number(self):
        datetime2jalali=str(self.time1)
        
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
       }

        for i,j in number.items():
            datetime2jalali=datetime2jalali.replace(i,j)
           
        
        
        return datetime2jalali
    def persian_number1(self):
  
        time1str=str(self.time2)
        
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
       }

        for i,j in number.items():
            time1str=time1str.replace(i,j)
        
        
        return time1str   
    @property
    def timeavg(self):
        if (self.dateexit > self.date):
            a=(self.dateexit-self.date).days
       
        
            return '{} {}'.format(a,'روز')
        else:


            time=jdatetime.datetime.time(self.time1)
            time3=jdatetime.datetime.time(self.time2)
            td1 =jdatetime.date.today()
            timefinal =str(jdatetime.datetime.combine(td1,time3)-jdatetime.datetime.combine(td1,time))
                
        
            number={
                '0':'۰',
                '1':'۱',
                '2':'۲',
                '3':'۳',
                '4':'۴',
                '5':'۵',
                '6':'۶',
                '7':'۷',
                '8':'۸',
                '9':'۹',
                'd':'ر',
                'a':'و',
                'y':'ز',
        }

            for i,j in number.items():
                timefinal=timefinal.replace(i,j)
        
            
        return  timefinal


    def dayrest(self):
        a=(self.dateexit-self.date).days
       
        
        return '{} {}'.format(a,'روز')
    
        



class Repmodel(models.Model):
    class Meta:
        verbose_name=' سیستم قطعات معیوب'
        verbose_name_plural='سیستم قطعات معیوب'
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name='نام کاربری')
    date=jmodels.jDateTimeField(default= datetime.now().replace(microsecond=0),verbose_name='تاریخ ثبت')
    name=models.ForeignKey(DeviceModel,null=True,on_delete=models.SET_NULL,max_length=150,verbose_name='نام قطعه')
    station=models.ForeignKey(StationModel,null=True,on_delete=models.SET_NULL,max_length=50,verbose_name='نام ایستگاه')
    subj=models.CharField(max_length=500,verbose_name='توضیحات')

   


    def time2time(self):        
            
        datetime2jalali=str(self.date.strftime("%Y-%m-%d %X"))
                
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
       }

        for i,j in number.items():
            datetime2jalali=datetime2jalali.replace(i,j)
        
            
        return datetime2jalali