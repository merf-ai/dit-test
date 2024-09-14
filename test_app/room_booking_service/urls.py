from django.urls import path

from room_booking_service.views import HelloApiView

urlpatterns = [path("hello/", HelloApiView.as_view())]
