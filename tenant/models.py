from django.db import models
from django.contrib.auth.models import User
from room.models import Room
    
    
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.phone})"