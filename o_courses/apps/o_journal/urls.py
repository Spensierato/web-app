from django.urls import path

from . import views


app_name = 'o_journal'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:student_id>/', views.detail, name = 'detail'),
	path('<int:student_id>/add_parents', views.add_parents, name = 'add_parents'),
	path('<int:group_id>/group_detail', views.group_detail, name = 'group_detail'),
	path('<int:group_id>/add_lesson', views.add_lesson, name = 'add_lesson'),
]