from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class contract(models.Model):
    start_contract=models.DateField('startdate',blank=False,null=False)
    end_contract=models.DateField('enddate',blank=True,null=True)
    company_num=models.ForeignKey('CompanyInfo',on_delete=models.PROTECT,blank=False,null=False)
    class Meta:
        db_table='contract'

class CompanyInfo(models.Model):
    business_num=models.CharField("Business Number",max_length=50,null=False)
    business_name=models.CharField("Name",max_length=50,blank=False,null=False)
    addr=models.CharField("Addr",max_length=255)
    addr_code=models.CharField("Addr_code",max_length=10)
    slug=models.SlugField('Slug',unique=True,allow_unicode=True,help_text='주소 슬러그')
    cls=models.CharField("Class",max_length=50)
    Email=models.CharField("E-mail",max_length=50)
    tel=models.CharField("Tel",max_length=50)
    fax=models.CharField("Fax",max_length=50)
    class Meta:
        db_table='company_info'

class CompanyUser(models.Model):
    company_num=models.ForeignKey("CompanyInfo",on_delete=models.PROTECT,null=True)
    ceo_name=models.CharField("Name",max_length=10,blank=False,null=False)
    manager=models.CharField("User",max_length=10)
    manage=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='manageid',blank=True,null=True)
    class Meta:
        db_table='company_user'

class Product(models.Model):
    product_name=models.CharField("name",max_length=50)
    price=models.IntegerField('price')
    unit=models.CharField("unit",max_length=10)
    class Meta:
        db_table='product'

class jobdiary(models.Model):
    job_day=models.DateField('job_day')
    visit=models.BooleanField('visit',)
    as_check=models.BooleanField('as',)
    owner=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='OWNER',blank=False,null=False)
    company_num=models.ForeignKey('CompanyInfo',on_delete=models.PROTECT,verbose_name='company',blank=False,null=False)
    title=models.CharField('title',max_length=100)
    content=models.TextField('CONTENT')
    creat_dt=models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt=models.DateTimeField('MODIFY DATA',auto_now=True)
    class Meta:
        db_table='jobdiary'