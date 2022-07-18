from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("business_name",'business_num')

@admin.register(models.CompanyUser)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("company_num",'ceo_name')


@admin.register(models.Product)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("product_name",'price')
    

@admin.register(models.contract)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("company_num",'start_contract','end_contract')


@admin.register(models.jobdiary)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("job_day",'title','company_num')