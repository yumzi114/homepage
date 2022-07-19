from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import category
from . import settings
import ipinfo
from shodan import Shodan


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip_api(ip_address=None):
        if ip_address[0:3]!="172" and ip_address[0:3]!="127":
                handler = ipinfo.getHandler(settings.IPINFO_TOKEN)
                details = handler.getDetails(ip_address)
                ip_data=details.all
                return ip_data
        else: return {}
def get_server(ip_address=None):
        api = Shodan('ifOlagHydJ2Ma93uWDh7qliJiTQdiGyE')
        try:
                host = api.host(ip_address)
        except Exception :return []
        else :
                setdata=[]
                [setdata.append(i) for i in host['data'] if host['data']]
                return setdata

class HomeViews(TemplateView):
    cteagorylist=category.objects.all()
    template_name='home.html'
    def get(self, request, *args,**kwargs):
        ip=get_client_ip(request)
        ip_data=get_ip_api(ip)
        severdata=get_server(ip)
        context={'categorys':self.cteagorylist,
                "severdata":severdata,

        }
        context.update(ip_data)
        return self.render_to_response(context)