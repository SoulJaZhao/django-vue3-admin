#文件backend/crud_demo/models.py

from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class NetworkIntrusionDetectionModel(CoreModel):
    module_name = models.CharField(max_length=255, verbose_name="模块名称")

    class Meta:
        db_table = "network_intrusion_detection"
        verbose_name = '网络入侵检测'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)