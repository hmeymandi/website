from datetime import date, datetime, time,timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model as user_model
from accounts.models import User
from django.db.models.fields import CharField
from django.urls import reverse
from jalali_date import datetime2jalali,date2jalali
from django.utils.text import slugify


import jdatetime
from django.db import models
from django_jalali.db import models as jmodels


from django.db.models import CharField, Model
from autoslug import AutoSlugField









User=user_model()




class Informationmodel(models.Model):
    class Meta:
        verbose_name='اطلاعات'
        verbose_name_plural='اطلاعات'
        ordering=['position']

    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=True,verbose_name='نمایش')
    position=models.IntegerField(verbose_name='موقیعت')

    def __str__(self) -> str:
        return self.title



class Reportmodel(models.Model):
    class Meta:
        verbose_name='گزارش'
        verbose_name_plural='گزارش'
       
    acepet_status=(('تایید نشده','تایید نشده'), 
                    ('تایید سر شیفت','تایید سر شیفت'),
                    ('تایید نهایی','تایید نهایی'),
    
    )

    shift_status=(('شیفت A','شیفت A'),
    ('شیفت B','شیفت B'),
    ('شیفت C','شیفت C'),)
    maintime=jdatetime.datetime.now
    subject=models.CharField(max_length=100,verbose_name='موضوع')
    categ=models.ManyToManyField(Informationmodel,verbose_name='دسته بندیُ',related_name='info')
    report=models.TextField(verbose_name='گزارش')
    date=jmodels.jDateTimeField(default=maintime,verbose_name='تاریخ ثبت',)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نام کاربری')
    shift=models.CharField(max_length=50,choices=shift_status,verbose_name='شیفت',null=True)
    acepet=models.CharField(max_length=30,choices=acepet_status,default='تایید نشده',verbose_name='وضیعت')
    slug=models.SlugField(unique=True,verbose_name='آدرس گزارش',blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date)
        super().save(*args, **kwargs)

    def __str__(self):

        return "{} {} {} {}".format(self.subject,self.date,self.user,self.shift)
    
    def get_absolute_url(self):
        return reverse("net:listreport")
    
    def get_absolute_url1(self):
        return reverse('net:detail',args=[self.slug])

  


    def __str__(self):
        return '{} {}'.format(self.subject, self.user)

    
    
    
    def persian_number(self):
        
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

    def timejalali(self):
        time=jdatetime.datetime(self.date)

        return time