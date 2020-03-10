from django.db import models

class Book(models.Model):
    vehicle_name=models.CharField(max_length=20)
    address=models.CharField(max_length=10)
    phone_no=models.TextField(max_length=15)

    def __str__(self):
        return self.vehicle_name +''+ self.address +''+ self.phone_no
