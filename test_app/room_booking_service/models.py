import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModels(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    birth_date = models.DateField(blank=True, null=True)


class UUIDModel(models.Model):
    id = models.CharField(max_length=16, default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True


class RoomImage(UUIDModel):
    path = models.ImageField()


class Room(UUIDModel):
    id = models.CharField(max_length=16, default=uuid.uuid4, primary_key=True)
    square = models.FloatField(verbose_name="Площадь комнаты", blank=True, null=True)
    number = models.IntegerField(verbose_name="Номер комнаты")
    description = models.TextField(blank=True, null=True)
    images = models.ManyToManyField(RoomImage)


class UserRoom(UUIDModel):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUserModels, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Дата начала бронирования")
    end_date = models.DateField(verbose_name="Дата конца бронирования")
    purpose_booking = models.TextField()
