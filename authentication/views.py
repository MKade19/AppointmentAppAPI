import jwt
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import User
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.CreateAPIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if user == None:
            return Response("user: User does not exist.", status=404)
        
        if not user.check_password(request.data['oldPassword']):
            return Response("Old password is not correct.", status=400)
        
        if request.data['newPassword'] != request.data['confirmPassword']:
            return Response("Passwords don't match.", status=400)
        
        user.set_password(request.data['newPassword'])
        user.save()

        return Response()