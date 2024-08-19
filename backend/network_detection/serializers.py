from network_detection.models import NetworkIntrusionModel
from dvadmin.utils.serializers import CustomModelSerializer


class NetworkIntrusionModelSerializer(CustomModelSerializer):
    """
    序列化器
    """
#这里是进行了序列化模型及所有的字段
    class Meta:
        model = NetworkIntrusionModel
        fields = "__all__"

#这里是创建/更新时的列化器
class NetworkIntrusionModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = NetworkIntrusionModel
        fields = '__all__'