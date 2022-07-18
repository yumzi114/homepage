from django.contrib import admin
from .models import category,Sites,BookList,InfoText
# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ("num",'category_name')

@admin.register(Sites)
class sitesAdmin(admin.ModelAdmin):
    list_display = ('site_name','category',)

@admin.register(InfoText)
class infoAdmin(admin.ModelAdmin):
    list_display = ('id','category',)
# Register your models here.

@admin.register(BookList)
class bookAdmin(admin.ModelAdmin):
    list_display = ('category','book_name',)