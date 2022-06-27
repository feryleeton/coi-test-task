from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from task_api.serializers import CategorySerializer, DoctorSerializer
from task_app.models import Category, Doctor
from rest_framework import viewsets, filters

# Create your views here.


class DoctorResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['birth_date', 'experience']

    def get_queryset(self):
        queryset = Doctor.objects.all()

        experience_gte = self.request.query_params.get('experience_gte')
        if experience_gte is not None:
            queryset = queryset.filter(experience__gte=experience_gte)

        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(categories__in=category)
    
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer