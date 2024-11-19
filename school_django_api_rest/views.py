from django.http import JsonResponse 
from school_django_api_rest.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer
from school_django_api_rest.models import Student, Course, Registration
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     student_id = data.get('student')
    #     course_id = data.get('course')
    #     period = data.get('period')

    #     student = Student.objects.get(id=student_id)
    #     course = Course.objects.get(id=course_id)

    #     registration = Registration.objects.create(
    #         student=student,
    #         course=course,
    #         period=period
    #     )

    #     serializer = RegistrationSerializer(registration)
    #     return JsonResponse(serializer.data)