from django.http import JsonResponse 
from school_django_api_rest.serializers import StudentSerializer, CourseSerializer
from school_django_api_rest.models import Student, Course
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer