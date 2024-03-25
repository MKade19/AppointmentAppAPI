from django.db import models
from users.models import User
from customers.models import Customer

class Appointment(models.Model):
    date = models.DateTimeField()
    start = models.TimeField()
    end = models.TimeField()
    employee = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)