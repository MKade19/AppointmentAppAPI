from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet 
from departments.views import DepartmentViewSet
from customers.views import CustomerViewSet
from roles.views import RoleViewSet
from appointments.views import AppointmentViewSet
from authentication.urls import urlpatterns as auth_urls

BASE_URL = 'appointment-app/api/'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('departments', DepartmentViewSet, basename='departments')
router.register('customers', CustomerViewSet, basename='customers')
router.register('roles', RoleViewSet, basename='roles')
router.register('appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include((router.urls, 'crud'))),
    path(BASE_URL + 'auth/', include((auth_urls, 'auth')))
]

urlpatterns += router.urls
