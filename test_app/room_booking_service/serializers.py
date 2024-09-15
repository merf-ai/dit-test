import rest_framework.serializers as serializers
from room_booking_service.models import UserRoom


class UserRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoom
        fields = "__all__"
