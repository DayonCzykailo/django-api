from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11)
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

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=1, blank=False, null=False, choices=LEVELS, default='B')

    def __str__(self) -> str:
        return self.code