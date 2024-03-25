from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from departments.serializers import DepartmentSerializer

class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["department"] = DepartmentSerializer(instance.department).data
        return data
    
    password = serializers.CharField(write_only=True, validators=[validate_password], required=False)

    class Meta:
        model = User
        fields = ('id', 'fullname', 'email', 'phone', 'department', 'address', 'password')

    def create(self, validated_data):
        if not 'password' in validated_data:
            raise serializers.ValidationError('Password must not be empty!')

        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['email'],
            fullname = validated_data['fullname'],
            phone = validated_data['phone'],
            address = validated_data['address'],
            department = validated_data['department'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("email", instance.username)
        instance.fullname = validated_data.get("fullname", instance.fullname)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.address = validated_data.get("address", instance.address)
        instance.department = validated_data.get("department", instance.department)

        if (validated_data.get("password", instance.password) != ''):
            instance.set_password(validated_data.get("password", instance.password))

        instance.save()
        return instance
    
class AppointmentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fullname')
        