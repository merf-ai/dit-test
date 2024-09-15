from django.urls import path

from room_booking_service.views import ReserveRoomView, RoomBookingScheduleView

urlpatterns = [
    path("room-booking-shedule/<str:pk>/", RoomBookingScheduleView.as_view()),
    path("reserve-room/", ReserveRoomView.as_view()),
]
