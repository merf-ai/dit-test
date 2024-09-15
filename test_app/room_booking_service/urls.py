from django.urls import path

from room_booking_service.views import RoomBookingScheduleView

urlpatterns = [
    path("room-booking-shedule/<str:pk>/", RoomBookingScheduleView.as_view())
]
