"""
购物项目的 WSGI 配置文件。

它将 WSGI 可调用对象暴露为名为 ``application`` 的模块级变量。

关于此文件的更多信息，请参阅：
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设置 Django 配置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')

# 获取 WSGI 应用程序
application = get_wsgi_application()
