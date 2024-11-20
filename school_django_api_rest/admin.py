from django.contrib import admin
from school_django_api_rest.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'phone')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'cpf', 'phone')
    list_per_page = 20
    search_fields = ('name', 'email', 'cpf', 'phone')
    ordering = ['name']

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code', 'description')
    search_fields = ('code', 'description', 'level')
    list_per_page = 20
    search_fields = ('code', 'description', 'level')
    ordering = ['code']


admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', 'student', 'course')
    search_fields = ('student', 'course', 'period')
    list_per_page = 20
    search_fields = ('student', 'course', 'period')
    ordering = ['student']

admin.site.register(Registration, Registrations)