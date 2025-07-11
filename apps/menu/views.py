from django.db.models.expressions import result
from django.http import JsonResponse
#from django.shortcuts import render
from django.views import View
import json
from apps.menu.models import MainMenu, SubMenu
from utils.ResponseMessage import MenuResponse

class ProductMainMenu(View):
    def get(self, request):
        print("get成功！")
        main_menu = MainMenu.objects.all()
        result_json = MenuResponse.success([m.to_json() for m in main_menu])
        return JsonResponse(result_json)

    def post(self, request):
        print("post成功")
        result_json = MenuResponse.failed("POST 请求失败")
        return JsonResponse(result_json)

class ProductSubMenu(View):
    def get(self, request):
        param_id = request.GET.get("main_menu_id")
        if not param_id:
            return JsonResponse(MenuResponse.failed("main_menu_id 参数缺失"), status=400)
        sub_menu_items = SubMenu.objects.filter(main_menu=param_id).select_related("main_menu")
        result_json = MenuResponse.success(
            [{"id": sm.id, "sub_menu_name": sm.sub_menu_name, "sub_menu_class": sm.sub_menu_class} for sm in sub_menu_items]
        )
        return JsonResponse(result_json)
