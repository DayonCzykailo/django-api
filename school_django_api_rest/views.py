from django.http import JsonResponse 
from school_django_api_rest.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListRegistrationCourseSerializer, StudentSerializerV2
from school_django_api_rest.models import Student, Course, Registration
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] # Only admin users can acess it
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    queryset = Student.objects.all()
    #serializer_class = StudentSerializer # because we have two versions of the serializer, we need to create a method to get the right one

    def get_serializer_class(self):
        print(f'Version: {self.request.version}')
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['code']
    search_fields = ['code', 'description']
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['student']
    search_fields = ['student', 'course']
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