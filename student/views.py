from django.shortcuts import render
from . import models
# Create your views here.


def student(request):
    student = models.Student.objects.filter(student=request.user).last()
    return render(request, 'student.html', {'student': student})


def attendances(request):
    student = models.Student.objects.filter(student=request.user).last()
    attendances = models.Attendance.objects.filter(student=student)
    return render(request, 'attendances.html', {'attendances': attendances})
    

def result(request):
    student = models.Student.objects.filter(student=request.user).last()
    results = models.Result.objects.filter(student=student)
    return render(request, 'result.html', {'results': results})
    
def exams(request):
    student = models.Student.objects.filter(student=request.user).last()
    exams = models.Exam.objects.filter(clas=student.clas, start_year=student.start_year)
    return render(request, 'exams.html', {'exams': exams})
    
def schedules(request):
    student = models.Student.objects.filter(student=request.user).last()
    schedules = models.Schedule.objects.filter(clas=student.clas, start_year=student.start_year)
    return render(request, 'schedules.html', {'schedules': schedules})
