import datetime
from .models import UserRoom


class RoomUserRepository:

    @staticmethod
    def get_room_is_free(room_pk):
        now_date = datetime.datetime.now()
        return not UserRoom.objects.filter(
            room__pk=room_pk, start_date__gte=now_date, end_date__lte=now_date
        ).exists()

    @staticmethod
    def get_booked_dates(queryset, start_booking_date, end_booking_date):
        return queryset.filter(
            start_date__lte=start_booking_date, end_date__gte=end_booking_date
        )
