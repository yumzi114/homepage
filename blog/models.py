from django.db import models

# Create your models here.
class category(models.Model):
    num = models.AutoField("NUM", primary_key=True)
    category_name = models.CharField("NAME", max_length=10, blank=False, unique=True)
    class Meta:
        db_table = "category"
        ordering = ("num",)
    def __str__(self):
        return self.category_name


class Sites(models.Model):
    category = models.ForeignKey("CATEGORY", on_delete=models.SET_NULL, null=True)
    site_url = models.URLField("URL", unique=True,null=False,blank=False)
    site_name=models.CharField("NAME",max_length=20,blank=True,null=True)
    site_detail=models.TextField(blank=True,null=True)
    class Meta:
        db_table = "site"
        ordering = ("-category",)

class BookList(models.Model):
    category = models.ForeignKey("CATEGORY", on_delete=models.SET_NULL, null=True)
    book_name=models.CharField("NAME",max_length=40,blank=False,null=False)
    book_url = models.URLField("URL", unique=True,null=True,blank=True)
    book_image=models.ImageField("IMAGE",upload_to='book/images/%Y/%m/%d/',blank=True)
    book_detail=models.TextField("TEXT",blank=True,null=True)
    class Meta:
        db_table = "booklist"
        ordering = ("-category",)

class InfoText(models.Model):
    category = models.ForeignKey("CATEGORY", on_delete=models.SET_NULL, null=True)
    # info_text=models.TextField("text",blank=True,null=True)
    content=models.TextField('CONTENT',blank=True,null=True)
    class Meta:
        db_table = "info"
        ordering = ("-category",)
    def __str__(self):
        return f'[{self.category}]'