from rest_framework import serializers
from school_django_api_rest.models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # other to way, its the same: ['id', 'name', 'email', 'cpf', 'birth_date', 'phone']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'description', 'level']