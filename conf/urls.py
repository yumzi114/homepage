"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views,settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeViews.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('webdb/', include('webdb.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',views.UserCreatView.as_view(),name='register'),
    path('accounts/register/done/',views.UserCreateDoneTV.as_view(),name='register_done'),
    path('server/net/',views.ServerNetViews.as_view(),name='servernet'),
    path('server/hw/',views.ServerHwViews.as_view(),name='serverhw'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)