from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.PositiveIntegerField(verbose_name="分类ID")
    store = models.ForeignKey("Store", on_delete=models.CASCADE, verbose_name="店铺ID")
    name = models.CharField(max_length=255, verbose_name="商品名称")
    description = models.TextField(blank=True, null=True, verbose_name="商品详情描述")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格")
    stock = models.PositiveIntegerField(default=0, verbose_name="库存数量")
    thumbnail = models.CharField(max_length=255, blank=True, null=True, verbose_name="商品缩略图")

    STATUS_CHOICES = [
        ("on_sale", "在售"),
        ("off_sale", "下架"),
        ("out_of_stock", "缺货"),
    ]
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default="on_sale", verbose_name="商品状态"
    )

    sales_volume = models.PositiveIntegerField(default=0, verbose_name="累计销量")
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览次数")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "product"
        verbose_name = "商品"
        verbose_name_plural = "商品"
        indexes = [
            models.Index(fields=["category_id"], name="idx_category"),
            models.Index(fields=["price"], name="idx_price"),
        ]

    def __str__(self):
        return self.name
