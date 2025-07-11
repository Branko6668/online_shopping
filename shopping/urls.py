"""
购物项目的 URL 配置。

`urlpatterns` 列表用于将 URL 路由到视图。更多信息请参考：
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

示例：
函数视图
    1. 添加导入： from my_app import views
    2. 添加 URL 路由： path('', views.home, name='home')

基于类的视图
    1. 添加导入： from other_app.views import Home
    2. 添加 URL 路由： path('', Home.as_view(), name='home')

包含其他 URL 配置
    1. 导入 `include()` 函数： from django.urls import include, path
    2. 添加 URL 路由： path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from apps.menu.views import ProductMainMenu, ProductSubMenu

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理 URL（已注释）
    path('main_menu/', ProductMainMenu.as_view(), name='main_menu'),
    path('sub_menu/', ProductSubMenu.as_view(), name='sub_menu'),
]
