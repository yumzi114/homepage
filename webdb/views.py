from django.shortcuts import render,redirect
from . import models
from blog.models import category
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


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

class ProductCreateView(CreateView):
    model=models.Product
    fields=['product_name','price','unit']
    success_url=reverse_lazy('webdb:productadd')
    extra=10
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = category.objects.all()
        return super(ProductCreateView, self).get_context_data(**kwargs)
    


# class ProductsCreateView(CreateView):
#     model=models.Product
#     fields=['product_name','price','unit']
#     success_url=reverse_lazy('webdb:productadds')
#     def get_context_data(self, **kwargs):
#         kwargs['formset'] = ProductsFormSet(instance=self.object)
#         kwargs['categorys'] = category.objects.all()
#         return super(ProductsCreateView, self).get_context_data(**kwargs)
#     def form_valid(self,form):
#         context=self.get_context_data()
#         formset=context['formset']
#         if formset.is_valid():
#             self.object=form.save()
#             formset.instance=self.object
#             formset.save()
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
