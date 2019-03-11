from django.db import models


# Create your models here.
class BusNOHistory(models.Model):
    BusNO = models.CharField(max_length=10)

    def __str__(self):
        return self.BusNO
