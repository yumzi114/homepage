from django.shortcuts import render,redirect
from . import models
from blog.models import category
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import ProductForm
from django.db import transaction


class CompanyCreateView(CreateView):
    model=models.CompanyInfo
    fields=['business_num','business_name','addr','slug','addr_code','cls','Email','tel','fax']
    initial={'slug':'주소 자동 슬러그'}
    success_url=reverse_lazy('webdb:companyadd')
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = category.objects.all()
        return super(CompanyCreateView, self).get_context_data(**kwargs)
    def form_valid(self,form):
        errorlist=[]
        if len(form.instance.business_num) !=10:
            errorlist.append('사업자번호는 10자리 형식입니다')
        if errorlist:
            form._errors = (f'{errorlist}'
                )
            return self.form_invalid(form)
        else: return super().form_valid(form)
        
class CompanyLV(ListView):
    model=models.CompanyInfo
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = category.objects.all()
        return super(CompanyLV, self).get_context_data(**kwargs)

# class ProductCreateView(CreateView):
#     model=models.Product
#     # fields=['product_name','price','unit']
#     fields=['product_name','price','unit']
#     success_url=reverse_lazy('webdb:productadd')
#     def get_context_data(self, **kwargs):
#         kwargs['categorys'] = category.objects.all()
#         return super(ProductCreateView, self).get_context_data(**kwargs)
#     def form_valid(self, form):
  
#         return super().form_valid(form)




def get_productadds(request):
    data=category.objects.all()
    context = {'categorys': data}
    if request.method == 'POST':
        form=ProductForm(request.POST,auto_id=False)
        product_name=request.POST.getlist('product_name')
        price=request.POST.getlist('price')
        unit=request.POST.getlist('unit')
        if form.is_valid():
            with transaction.atomic():
                for i in range(len(product_name)):
                    form=ProductForm(request.POST,auto_id=False)
                    post = form.save()
                    post.product_name=product_name[i]
                    post.price=price[i]
                    post.unit=unit[i]
                    post.save()
                return HttpResponseRedirect('/webdb/product/add/')
        else:
            pass
    else:
        return render(request, 'webdb/product_form.html',context)

class ProductLV(ListView):
    model=models.Product
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = category.objects.all()
        return super(ProductLV, self).get_context_data(**kwargs)

