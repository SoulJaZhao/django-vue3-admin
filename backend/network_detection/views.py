from django.shortcuts import render
# Create your views here.
from network_detection.models import NetworkIntrusionModel
from network_detection.serializers import NetworkIntrusionModelSerializer, NetworkIntrusionModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class NetworkIntrusionModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = NetworkIntrusionModel.objects.all()
    serializer_class = NetworkIntrusionModelSerializer
    create_serializer_class = NetworkIntrusionModelCreateUpdateSerializer
    update_serializer_class = NetworkIntrusionModelCreateUpdateSerializer