from django.http import JsonResponse 
from school_django_api_rest.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListRegistrationCourseSerializer
from school_django_api_rest.models import Student, Course, Registration
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] # Only admin users can acess it
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationStudentViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListRegistrationStudentSerializer

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk']) # get the id from the url
        return queryset
    
class ListRegistrationCourseViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListRegistrationCourseSerializer

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset