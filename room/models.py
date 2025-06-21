from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    room_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    room_description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room_name} - {self.room_price} VNĐ"