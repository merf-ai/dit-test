from rest_framework import filters
from .utils import RoomUserRepository


class DataBookingFilter(filters.BaseFilterBackend):
    """Фильтр для получения бронирования на определённый период времени"""

    def filter_queryset(self, request, queryset, view):
        start_booking_date = request.query_params.get("start_date")
        end_booking_date = request.query_params.get("end_date")
        if start_booking_date and end_booking_date:
            rep = RoomUserRepository()
            return rep.get_booked_dates(queryset, start_booking_date, end_booking_date)
        return queryset
