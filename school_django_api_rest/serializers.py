from rest_framework import serializers
from school_django_api_rest.models import Student, Course, Registration
from school_django_api_rest.validations import validate_phone_is_brazil_format, validate_cpf_value
# you can use faker library to test. https://faker.readthedocs.io/en/master/
# you can use too the FactoryBoy library to test. https://factoryboy.readthedocs.io/en/stable/

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # other to way, its the same then: ['id', 'name', 'email', 'cpf', 'birth_date', 'phone']

    # this is a generic validation for all fields, here we can get all fields and validate them
    # def validate(self, attrs): 
    #     if not attrs["name"].isalpha():
    #         raise serializers.ValidationError({'name':'Only letters are allowed.'})

    def validate_cpf(self, value): # this is a custom validation for the cpf field
        if not value.isdigit():
            raise serializers.ValidationError({'cpf':'Only numbers are allowed.'})
        if len(value) != 11:
            raise serializers.ValidationError({'cpf':'CPF must have 11 digits.'})
        if validate_cpf_value(value):
            raise serializers.ValidationError({'cpf':'Invalid CPF.'})
        return value
    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError({'name':'Only letters are allowed.'})
        return value
    
    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError({'phone':'Only numbers are allowed.'})
        if len(value) == 14:
            raise serializers.ValidationError({'phone':'Phone must have 14 digits.'})
        if validate_phone_is_brazil_format(value):
            raise serializers.ValidationError({'phone':'Phone must be in the format XX XX XXXXX-XXXX.'})
        return value
    

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

class StudentSerializerV2(serializers.ModelSerializer): # this is a versionament of the StudentSerializer
    class Meta:
        model = Student 
        fields = ['name', 'email', 'cpf']
