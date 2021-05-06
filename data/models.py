from django.db import models

# Create your models here.
class SmartFarmData(models.Model):
    dataNum = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add = True)
    outTemp = models.FloatField()
    inTemp = models.FloatField()
    outHumidity = models.FloatField()
    inHumidity = models.FloatField()
    co2ppm = models.FloatField()
    src = models.TextField()
    
    class Meta:
      	ordering = ['id']
        # id순으로 정렬명령어 # ordering = ['-id']

    def __str__(self):
        return self.dataNum