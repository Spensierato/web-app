from .models import Group, Student, Lesson, Exam, Parents, Homework

import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def index(request):
	students_list = Student.objects.order_by('group_number')
	groups_list = Group.objects.order_by('group_number')
	context = {'students_list': students_list, 'groups_list': groups_list}
	
	return render(request, 'o_journal/list.html', context)


def detail(request, student_id):
	try:
		student = Student.objects.get( id = student_id )
	except:
		raise Http404("Ученик не найден")

	parents_fios = student.parents_set.order_by('id')

	return render(request, 'o_journal/detail.html', {'student': student, 'parents_fios': parents_fios})


def add_parents(request, student_id):
	try:
		student = Student.objects.get( id = student_id )
	except:
		raise Http404("Ученик не найден")

	student.parents_set.create(parents_fio = request.POST['name'], parents_contacts = request.POST['text'])

	return HttpResponseRedirect( reverse('o_journal:detail', args = (student.id,)) )


def group_detail(request, group_id):
	students_list = Student.objects.filter(group_number = group_id)
	lesson_list = Lesson.objects.filter(group_number = group_id)
	homework_list = Homework.objects.filter(group_number = group_id)
	exam_list = Exam.objects.filter(group_number = group_id)
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	return render(request, 'o_journal/group_detail.html', {'group': group, 
		'students_list': students_list, 
		'lesson_list': lesson_list, 
		'homework_list': homework_list, 
		'exam_list': exam_list} 
		)


def add_lesson(request, group_id):
	students_list = Student.objects.filter( group_number = group_id)
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	group.lesson_set.create(theme = request.POST['name'], date = timezone.now() )

	return render( request, 'o_journal/lesson.html', {'group': group, 'students_list': students_list} )


def lesson_detail(request, lesson_id):
	try:
		lesson = Lesson.objects.get( id = lesson_id )
	except:
		raise Http404("Урок не найден")
	students_list = Student.objects.filter( group_number = group_id)
	return render( request, 'o_journal/lesson.html', {'lesson': lesson, 'students_list': students_list} )


def add_homework(request, group_id):
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	group.homework_set.create(hw_theme = request.POST['name'], homework = request.POST['text'], hw_date = request.POST['date'])

	return HttpResponseRedirect( reverse('o_journal:group_detail', args = (group.id,)) )


def add_exam(request, group_id):
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	group.exam_set.create(exam_work_title = request.POST['name'], exam_work_text = request.POST['text'] )

	return HttpResponseRedirect( reverse('o_journal:group_detail', args = (group.id,)) )
