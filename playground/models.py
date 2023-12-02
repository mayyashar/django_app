from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    healthy = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('Other', 'Other')])
    fever = models.CharField(max_length=100)
    Blood_Pressure = models.CharField(max_length=100)
    specify = models.CharField(max_length=100)
