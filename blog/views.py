
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models
# Create your views here.
class SitesLV(ListView):
    model=models.Sites
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = models.category.objects.all()
        kwargs['categorysname'] = models.category.objects.filter(num=self.kwargs['pk'])
        kwargs['object_list'] = models.Sites.objects.filter(category_id=self.kwargs['pk'])
        return super(SitesLV, self).get_context_data(**kwargs)
    
 


class BookLV(ListView):
    model=models.BookList
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = models.category.objects.all()
        kwargs['categorysname'] = models.category.objects.filter(num=self.kwargs['pk'])
        kwargs['object_list'] = models.BookList.objects.filter(category_id=self.kwargs['pk'])
        return super(BookLV, self).get_context_data(**kwargs)
    

class CategoryInfo(DetailView):
    model=models.InfoText
    def get_context_data(self, **kwargs):
        kwargs['categorys'] = models.category.objects.all()
        kwargs['categorysname'] = models.category.objects.filter(num=self.kwargs['pk'])
        return super(CategoryInfo, self).get_context_data(**kwargs)

# def infodetail(request,pk):
#     post=models.InfoText.objects.get(pk=pk)
#     categorys=models.category.objects.all()
#     return render(request,'blog/infotext_detail.html',{'post':post,'categorys':categorys})