from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    permission_department = models.CharField(max_length=50)
    permission_employee = models.CharField(max_length=50)
    permission_appointment = models.CharField(max_length=50)
    permission_customer = models.CharField(max_length=50)
