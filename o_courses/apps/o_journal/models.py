import datetime

from django.db import models
from django.utils import timezone

class Group(models.Model):
	group_number = models.IntegerField("Номер группы", default=0)

	def __str__(self):
		return f'Номер группы: {self.group_number}'

	class Meta:
		verbose_name = "Группа"
		verbose_name_plural = 'Группы'

class Student(models.Model):
	first_name = models.CharField("Имя", max_length=50)
	middle_name = models.CharField("Отчество", max_length=50)
	last_name = models.CharField("Фамилия", max_length=50)
	group_number = models.ForeignKey(Group, on_delete = models.CASCADE)
	email = models.EmailField("Email")
	av_grade = models.IntegerField("Средняя оценка", default=0)

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.middle_name}, {self.group_number}, Email: {self.email}'

	class Meta:
		verbose_name = "Ученик"
		verbose_name_plural = 'Ученики'


class Lesson(models.Model):
	date = models.DateField()
	theme = models.CharField("Тема урока", max_length=200)
	group_number = models.ForeignKey(Group, on_delete = models.CASCADE)
	presence = models.BooleanField("Присутствие", default=False)
	grade = models.IntegerField("Оценка", default=0)

	def __str__(self):
		return f'"Дата:"{self.date}, "Группа:" {self.group_number}, "Тема:"{self.theme}'

	class Meta:
		verbose_name = "Урок"
		verbose_name_plural = 'Уроки'

class Homework(models.Model):
	hw_theme = models.CharField("Тема домашнего задания", max_length=200)
	group_number = models.ForeignKey(Group, on_delete = models.CASCADE)
	homework = models.TextField("Текст домашнего задания")
	hw_date = models.DateField()
	hw_grade = models.IntegerField("Оценка за домашнее задание", default=0)
	hw_done = models.BooleanField("Выполнено ли ДЗ", default=False)

	def __str__(self):
		return f'"Дедлайн:"{self.hw_date}, "Тема:" {self.hw_theme}, "Задание:" {self.homework}'

	class Meta:
		verbose_name = "Домашнее задание"
		verbose_name_plural = 'Домашние задания'

class Parents(models.Model):
	st_name = models.ForeignKey(Student, on_delete = models.CASCADE)
	parents_fio = models.TextField("ФИО родителей")
	parents_contacts = models.TextField("Контакты родителей")

	def __str__(self):
		return f' Ученик: {self.st_name}, ФИО родителей: {self.parents_fio}, Контакты: {self.parents_contacts}'

	class Meta:
		verbose_name = "Родители"
		verbose_name_plural = 'Родители'

class Exam(models.Model):
	group_number = models.ForeignKey(Group, on_delete = models.CASCADE)
	exam_work_title = models.CharField("Тема контрольно работы", max_length=200)
	exam_work_text = models.TextField("Текст контрольной работы")
	exam_work_grade = models.IntegerField("Оценка за контрольную работу", default=0)
	exam_work_done = models.BooleanField("Сдано", default=False)

	def __str__(self):
		return f'"Тема: "{self.exam_work_title}, "Задание: "{self.exam_work_text} '

	class Meta:
		verbose_name = "Контрольная работа"
		verbose_name_plural = 'Контрольные работы'
	
	

	