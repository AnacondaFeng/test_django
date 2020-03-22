import os
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
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
