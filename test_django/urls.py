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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from test_django import views

# 内置视图错误处理，重写500页面
handler500 = 'test_django.views.page_500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #     展示当前时间
    url(r'^time/$', views.now_time),
    url(r'article/(?P<year>[0-9]{4})/$', views.article, name='article_detail'),

    #     读取文件方式展示，页面从html加载
    url(r'now/$', views.now_use_file),

    #     重定向试验
    url(r'^index1/$', views.index_one, name='index_one'),
    url(r'^index2/$', views.index_two, name='index_two'),

#     测试页面
    url(r'$', views.test_page, name='test_page')
]

# 添加自定义的静态资源目录访问
urlpatterns += [url(r'^medias/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT
})]
