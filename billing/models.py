from django.db import models
from room.models import Room
from decimal import Decimal, InvalidOperation

class Bill(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    month = models.DateField(help_text="Chọn ngày đầu tháng")
    electricity = models.PositiveIntegerField(help_text="Số ký điện (kWh)")
    water = models.PositiveIntegerField(help_text="Số nước (m³)")
    electricity_rate = models.DecimalField(max_digits=6, decimal_places=2, default=3000, null=False, blank=False)
    water_rate = models.DecimalField(max_digits=8, decimal_places=2, default=15000, null=False, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            electricity = Decimal(str(self.electricity))
            water = Decimal(str(self.water))
            rate_elec = Decimal(str(self.electricity_rate))
            rate_water = Decimal(str(self.water_rate))
            self.total = electricity * rate_elec + water * rate_water + self.room.room_price
        except (InvalidOperation, TypeError, ValueError) as e:
            print("❌ Decimal error:", e)
            self.total = Decimal(0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Hóa đơn {self.room.room_name} - {self.month.strftime('%m/%Y')}"
