from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    object_list = Student.objects.all()
    template = 'school/students_list.html'
    context = {'object_list': object_list}
    for student in object_list:
        print(f'firts {student.name}')
        for teacher in student.teachers.all():
            print(f'second {teacher.name}, {teacher.subject}')


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
