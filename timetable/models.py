from django.db import models
from model_utils import Choices

# Create your models here.

class Area(models.Model):
    area = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.area.upper()

class AreaCode(models.Model):
    code = models.CharField(max_length=4, null=True)
    # area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Schedule(models.Model):
    DAYS = Choices('Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday')
    STAGE = Choices('ONE', 'TWO')
    PEAK  = Choices('AM', 'PM')
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    code = models.ForeignKey('AreaCode', on_delete=models.CASCADE) 
    day = models.CharField(choices=DAYS, default = DAYS.Monday, max_length = 20)
    stage = models.CharField(choices=STAGE, default = STAGE.ONE, max_length=20)
    peak = models.CharField(choices=PEAK, default = PEAK.AM, max_length=2)
