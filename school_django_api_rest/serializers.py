from rest_framework import serializers
from school_django_api_rest.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # other to way, its the same then: ['id', 'name', 'email', 'cpf', 'birth_date', 'phone']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'description', 'level']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__' # ['id', 'student', 'course', 'period']

class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display() # get the value of the field period in the model Registration

class ListRegistrationCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    
    class Meta:
        model = Student
        fields = ['student']