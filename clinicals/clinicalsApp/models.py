from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName = models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    age=models.IntegerField()

class ClinicalData(models.Model):
    componentName=models.CharField(max_length=20)
    componentValue=models.CharField(maxmax_length=20)
    measuredDateTime=models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    
