#!/usr/bin/env python
"""Django 的命令行工具，用于执行管理任务。"""
import os
import sys


def main():
    """运行管理任务。"""
    # 设置 Django 的默认配置模块
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')
    try:
        # 导入 Django 的命令行执行函数
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django。请确认它已安装，"
            "并且可以通过 PYTHONPATH 环境变量找到？"
            "你是否忘记激活虚拟环境？"
        ) from exc
    # 执行命令行指令
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
