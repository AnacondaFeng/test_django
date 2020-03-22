"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from test_django import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#     展示当前时间
    url(r'^time/$', views.now_time),
    url(r'article/(?P<year>[0-9]{4})/$', views.article, name='article_detail'),

#     读取文件方式展示，页面从html加载
    url(r'now/$', views.now_use_file)

]