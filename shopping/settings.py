"""
购物项目的 Django 配置文件。

使用 Django 5.2.1 通过 'django-admin startproject' 生成。

关于此文件的更多信息，请参阅：
https://docs.djangoproject.com/en/5.2/topics/settings/

完整的配置选项和对应值请查看：
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
import os, sys
from pathlib import Path

# 构建项目路径，例如： BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 快速开发设置 - 不适用于生产环境
# 参考：https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# 安全警告：请在生产环境中保密此密钥！
SECRET_KEY = 'django-insecure-pz^bikli3lpv+&9e)u0zonc(o_rsha(5)4+h5vwvmpzm@o&@))'

# 安全警告：生产环境不要开启调试模式！
DEBUG = True

# 允许访问的主机列表
ALLOWED_HOSTS = []


# 应用定义

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'apps.user',
    'apps.menu',
]

# 允许所有域名跨域
CORS_ORIGIN_ALLOW_ALL = True
# 允许携带cookie
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",  # 正确的本地地址
    "http://localhost:8000",  # 允许 localhost 访问
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',  # 安全中间件
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话中间件
    'django.middleware.common.CommonMiddleware',  # 通用中间件
    #'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 保护
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 认证中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止点击劫持
]

# 根 URL 配置
ROOT_URLCONF = 'shopping.urls'

# 模板设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 指定模板文件夹
        'APP_DIRS': True,  # 启用应用模板目录
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # 请求上下文处理器
                'django.contrib.auth.context_processors.auth',  # 认证上下文处理器
                'django.contrib.messages.context_processors.messages',  # 消息上下文处理器
            ],
        },
    },
]

# WSGI 应用程序
WSGI_APPLICATION = 'shopping.wsgi.application'


# 数据库配置
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用 mysql 数据库
        'NAME': 'shopping',  # 数据库文件路径
        'USER': 'root',
        'PASSWORD': '200249',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# 密码验证
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # 用户属性相似性验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 最小长度验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 常见密码验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 数字密码验证
    },
]


# 国际化设置
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 语言代码（简体中文）
TIME_ZONE = 'UTC'  # 时区设置（世界协调时间 UTC）
USE_I18N = True  # 启用国际化支持
USE_TZ = True  # 启用时区支持

# 静态文件（CSS、JavaScript、图片）
# 随便访问一个图片 http://localhost:8080/static/product_images/268357.jpg
# 参考：https://docs.djangoproject.com/en/5.2/howto/static-files/
# 静态文件访问路径
STATIC_URL = 'static/'
# 配置静态文件目录
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 默认主键类型
# 参考：https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'