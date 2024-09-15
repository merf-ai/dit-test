from collections import OrderedDict
import csv
import os
from django.core.management import BaseCommand
from django.db import transaction
from room_booking_service.models import (
    CustomUser,
    Room,
    RoomImage,
    RoomImagesManyToMany,
    UserRoom,
)
from test_app.settings import BASE_DIR

data = OrderedDict(
    (
        (CustomUser, "CustomUser.csv"),
        (Room, "Room.csv"),
        (UserRoom, "UserRoom.csv"),
        (RoomImage, "RoomImage.csv"),
        (RoomImagesManyToMany, "RoomImagesManyToMany.csv"),
    )
)


def get_data_from_file(file_name):
    with open(BASE_DIR / "test_data" / file_name, "r", encoding="utf-8-sig") as fin:
        dr = csv.DictReader(
            fin,
        )
        return [dt for dt in dr]


class Command(BaseCommand):

    def handle(self, *args, **options):
        with transaction.atomic():
            for model, filename in data.items():
                prepared_data = get_data_from_file(filename)
                if model is UserRoom:
                    prepared_data = [
                        {
                            **dt,
                            "room": Room.objects.get(id=dt.get("room")),
                            "user": CustomUser.objects.get(id=dt.get("user")),
                        }
                        for dt in prepared_data
                    ]
                elif model is RoomImage:
                    for dt in prepared_data:
                        RoomImage.objects.create(
                            id=dt.get("id"), path=os.path.abspath(dt.get("path"))
                        )
                    continue
                elif model is RoomImagesManyToMany:
                    prepared_data = [
                        {
                            **dt,
                            "room": Room.objects.get(id=dt.get("room")),
                            "image": RoomImage.objects.get(id=dt.get("image")),
                        }
                        for dt in prepared_data
                    ]
                model.objects.bulk_create([model(**dt) for dt in prepared_data])
