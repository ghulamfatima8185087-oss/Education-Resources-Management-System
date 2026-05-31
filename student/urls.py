from django.urls import path
from . import views
urlpatterns = [
    path('student', views.student, name="student"),
    path('attendances', views.attendances, name="attendances"),
    path('result', views.result, name="result"),
    path('exams', views.exams, name="exams"),
    path('schedules', views.schedules, name="schedules"),

]