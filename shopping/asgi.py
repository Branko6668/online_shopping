"""
购物项目的 ASGI 配置文件。

它将 ASGI 可调用对象暴露为名为 ``application`` 的模块级变量。

关于此文件的更多信息，请参阅：
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 设置 Django 配置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')

# 获取 ASGI 应用程序
application = get_asgi_application()
