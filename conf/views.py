from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import category

class HomeViews(TemplateView):
    cteagorylist=category.objects.all()
    template_name='home.html'
    def get(self, request, *args,**kwargs):
        context={'categorys':self.cteagorylist,

        }
        return self.render_to_response(context)