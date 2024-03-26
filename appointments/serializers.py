from rest_framework import serializers
from .models import Appointment
from customers.serializers import CustomerSerializer
from users.serializers import AppointmentUserSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["customer"] = CustomerSerializer(instance.customer).data
        data["employee"] = AppointmentUserSerializer(instance.employee).data
        return data
    
    class Meta:
        model = Appointment
        fields = '__all__'