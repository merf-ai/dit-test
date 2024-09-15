import rest_framework.serializers as serializers
from room_booking_service.models import UserRoom


class UserRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoom
        fields = "__all__"


class ReserveRoomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = UserRoom
        exclude = ("id",)
