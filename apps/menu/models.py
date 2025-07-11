import json
from django.db import models

class MainMenu(models.Model):
    id = models.AutoField(primary_key=True)
    main_menu_name = models.CharField(max_length=50, verbose_name="主菜单名称")
    main_menu_class = models.PositiveIntegerField(verbose_name="主菜单分类")

    class Meta:
        db_table = "main_menu"
        verbose_name = "主导航菜单"
        verbose_name_plural = "主导航菜单"
        indexes = [
            models.Index(fields=["main_menu_class"], name="idx_main_menu_class"),
        ]

    def __str__(self):
        return f"{self.main_menu_name} ({self.main_menu_class})"

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "main_menu_name": self.main_menu_name,
            "main_menu_class": self.main_menu_class
        }, ensure_ascii=False)

class SubMenu(models.Model):
    id = models.AutoField(primary_key=True)  # 二级菜单自身的 ID
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, verbose_name="主菜单")
    sub_menu_name = models.CharField(max_length=50, verbose_name="二级菜单名称")
    sub_menu_class = models.CharField(max_length=50, verbose_name="二级菜单分类")

    class Meta:
        db_table = "sub_menu"
        verbose_name = "二级菜单"
        verbose_name_plural = "二级菜单"
        indexes = [
        models.Index(fields=["main_menu"], name="idx_main_menu"),
        ]

    def __str__(self):
        return f"{self.main_menu.main_menu_name} - {self.sub_menu_name}"

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "main_menu_id": self.main_menu.id,  # 仍然可以通过外键获取主菜单的 ID
            "main_menu_name": self.main_menu.main_menu_name,
            "main_menu_class": self.main_menu.main_menu_class,
            "sub_menu_name": self.sub_menu_name,
            "sub_menu_class": self.sub_menu_class
        }, ensure_ascii=False)

