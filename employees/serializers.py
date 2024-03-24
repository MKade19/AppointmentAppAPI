from rest_framework import serializers
from .models import Employee
from departments.serializers import DepartmentSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["department"] = DepartmentSerializer(instance.department).data
        return data

    class Meta:
        model = Employee
        fields = '__all__'
        