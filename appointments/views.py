from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer


class CustomPagination(PageNumberPagination):
    # page_size = 5
    page_size_query_param = 'page_count'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })
    

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer
    pagination_class = CustomPagination
