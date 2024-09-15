from rest_framework.generics import ListAPIView
from .serializers import UserRoomSerializer
from .models import UserRoom
from .filters import DataBookingFilter
from test_app.pagination import StandardResultsSetPagination
from .utils import RoomUserRepository


# Create your views here.
class RoomBookingScheduleView(ListAPIView):
    """Вьюхя для получения записей о бронировании переговорной комнаты на текущий день (либо на определенное время)"""

    serializer_class = UserRoomSerializer
    queryset = UserRoom.objects.all()
    filter_backends = [DataBookingFilter]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        room_pk = self.kwargs.get("pk")
        return UserRoom.objects.filter(room__pk=room_pk)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        room_pk = self.kwargs.get("pk")
        user_room_rep = RoomUserRepository
        response.data["is_free"] = user_room_rep.get_room_is_free(room_pk)
        return response
