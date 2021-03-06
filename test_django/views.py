import os
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from test_django.settings import BASE_DIR


def now_time(request):
    """展示系统当前的时间"""
    now = datetime.now()
    # html = 'now:{0}'.format(now)
    html = """
    <html>
        <head>
            <style type="text/css">
                body{{
                    color:red;
                    }}
            </style>
            <body>
                now:{0}
            </body>
        </head>
    </html>
    """.format(now)
    return HttpResponse(html)


def article(request, year):
    """获取URL中的参数"""
    print('year:{0}'.format(year))
    # 获取get参数中月份
    # 如果没有这个参数默认值是None
    month = request.GET.get('month', None)
    print('month:{0}'.format(month))
    # 强制发生异常，测试500错误
    raise ValueError
    return HttpResponse('article:' + year)


def now_use_file(request):
    """使用文件的方式，页面读取来，并响应"""
    html = ''
    # file_name = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    # with open(file_name) as f:
    #     html = f.read()

    # 使用loader读取
    now = datetime.now()
    # temp = loader.get_template('index.html')
    # html = temp.render(
    #     {
    #         'now':now
    #     }
    # )
    # return HttpResponse(html)

    # 直接使用render，这种方法应该是最好了
    return render(request, 'index.html', {
        'now': now
    })


def index_one(request):
    """访问该视图时重定向index two"""
    # return HttpResponse('index one')
    # return HttpResponseRedirect('/index2/')
    # 使用reversed定位url name
    # url = reversed('index_two')
    return redirect('index_two')

def index_two(request):
    return HttpResponse('index two')

def page_500(request):
    """重写500响应页面"""
    return HttpResponse('服务器异常！！！')
