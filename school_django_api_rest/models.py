from django.db import models
from django.core.validators import MinLengthValidator # https://docs.djangoproject.com/en/5.0/ref/validators/

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    LEVELS = [
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]

    code = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(limit_value=3)])
    description = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=1, blank=False, null=False, choices=LEVELS, default='B')

    def __str__(self) -> str:
        return self.code
    
class Registration(models.Model):
    PERIODS = [
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
        ('D', 'Dawn')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    period = models.CharField(max_length=1, blank=False, null=False, choices=PERIODS, default='M')

    def __str__(self) -> str:
        return f'{self.student.name} - {self.course.code}'