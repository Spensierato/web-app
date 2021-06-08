from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Group, Student, Lesson, Exam, Parents, Homework
import datetime
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
	students_list = Student.objects.filter( group_number = group_id)
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	return render(request, 'o_journal/group_detail.html', {'group': group, 'students_list': students_list} )


def add_lesson(request, group_id):
	students_list = Student.objects.filter( group_number = group_id)
	try:
		group = Group.objects.get( id = group_id)
	except:
		raise Http404("Группа не найдена")

	group.lesson_set.create(theme = request.POST['name'], date = timezone.now())

	return render( request, 'o_journal/lesson.html', {'group': group, 'students_list': students_list} ) 