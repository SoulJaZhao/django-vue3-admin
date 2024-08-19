from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class NetworkIntrusionModel(CoreModel):
    node_name = models.CharField(max_length=255, verbose_name="节点名称")

    class Meta:
        db_table = "edge_node"
        verbose_name = '边缘节点表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
