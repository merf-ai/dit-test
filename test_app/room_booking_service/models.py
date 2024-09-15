import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class UUIDModel(models.Model):
    id = models.CharField(max_length=16, default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    id = models.CharField(max_length=16, default=uuid.uuid4, primary_key=True)
    middle_name = models.CharField(max_length=150, blank=True)
    birth_date = models.DateField(blank=True, null=True)


class RoomImage(UUIDModel):
    path = models.ImageField()


class Room(UUIDModel):
    square = models.FloatField(verbose_name="Площадь комнаты", blank=True, null=True)
    number = models.IntegerField(verbose_name="Номер комнаты")
    description = models.TextField(blank=True, null=True)
    images = models.ManyToManyField(
        through="RoomImagesManyToMany", through_fields=("room", "image"), to=RoomImage
    )


class RoomImagesManyToMany(UUIDModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ForeignKey(RoomImage, on_delete=models.CASCADE)


class UserRoom(UUIDModel):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Дата начала бронирования")
    end_date = models.DateField(verbose_name="Дата конца бронирования")
    purpose_booking = models.TextField()
