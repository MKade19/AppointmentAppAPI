from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from employees.models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class UserTokenSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [ 'id', 'email' ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # These are claims, you can add custom claims
        token['email'] = user.email
        token['verified'] = user.profile.verified
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] =  UserTokenSerializer(self.user).data
    
        return data 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmPassword = serializers.CharField(write_only=True, required=True)
    # employee = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirmPassword')


    def validate(self, attrs):
        if attrs['password'] != attrs['confirmPassword']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        employee_from_db = Employee.objects.filter(email=validated_data['email']).first()
        
        if employee_from_db == None:
            raise serializers.ValidationError({ "employee": "Employee does not exist." })

        user = User.objects.create(
            email = validated_data['email'],
            employee = employee_from_db,
            username = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user