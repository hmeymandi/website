from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django_jalali.db import models as jmodels

class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,idcart,phone,email,address,shift,password,date):
             
        if not password:
            raise ValueError('plz password')        
    




        user=self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name,
        idcart=idcart,phone=phone,address=address,shift=shift,password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,idcart,phone,email,address,shift,password,date):
        user=self.create_user(first_name,last_name,idcart,phone,email,address,shift,password,date)
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        verbose_name = 'وضیعت کاربری'
        verbose_name_plural='وضیعت کاربری'
    shift_status=((' A شیفت ',' A شیفت '),(' B شیفت ',' B شیفت '),
                (' C شیفت ',' C شیفت '),

    )
    first_name=models.CharField(max_length=100,verbose_name='نام')
    last_name=models.CharField(max_length=100,verbose_name='نام خانوادگی')
    idcart=models.CharField(max_length=10,unique=True,verbose_name='شماره ملی(شناسه کاربری)')
    phone=models.CharField(max_length=11,verbose_name='تلفن همراه')
    email=models.EmailField(blank=True,unique=True,verbose_name='ایمیل')
    address=models.CharField(max_length=250,verbose_name='آدرس')
    shift=models.CharField(max_length=10,choices=shift_status,blank=True,null=True,verbose_name='شیفت')
    date=jmodels.jDateField(null=True,verbose_name='تاریخ استخدام')
    
    
    is_active=models.BooleanField(default=True,verbose_name='کاربر عادی')
    is_admin=models.BooleanField(default=False,verbose_name='مدیر')
    is_authe=models.BooleanField(default=False,verbose_name='سرشیفت')
    is_manager=models.BooleanField(default=False,verbose_name='سرپرست')
    is_nazer=models.BooleanField(default=False,verbose_name='ناظر')
    
    USERNAME_FIELD='idcart'
    REQUIRED_FIELDS=['first_name','last_name','phone','email','address','shift','date']
    object=UserManager()

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


    def has_perm(self, perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin  
    

        
