from django.contrib import admin

from .models import Student, Lesson, Homework, Parents, Exam, Group

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Homework)
admin.site.register(Parents)
admin.site.register(Exam)