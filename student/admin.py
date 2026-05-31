from django.contrib import admin
from . import models
# Register your models here.


# admin.site.register(models.Course)
# admin.site.register(models.Student)

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'start_year', 'end_year', 'gender', 'religion', 'course', 'is_completed', 'is_degree_issued')
    list_filter = ('start_year', 'end_year', 'clas')
    search_fields = ('std_name',)


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'year', 'month', 'lectures', 'attended', 'leaves', 'absents')
    list_filter = ('year', 'month')

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'clas', 'start_year', 'end_year', 'exam_name', 'subject', 'date_time')
    list_filter = ('course', 'clas', 'start_year', 'end_year', 'exam_name')
    



@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_marks', 'obtained_marks')
    list_filter = ('total_marks', 'obtained_marks')



@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'clas', 'start_year', 'end_year', 'schedule_name', 'subject', 'teacher', 'day', 'time')
    list_filter = ('course', 'clas', 'start_year', 'end_year', 'schedule_name')
    

