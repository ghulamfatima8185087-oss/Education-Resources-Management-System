from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_year = models.PositiveSmallIntegerField(blank=True, null=True)
    end_year = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    course = models.CharField(max_length=50, blank=True, null=True)
    clas = models.CharField(max_length=50, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    course_fee = models.PositiveSmallIntegerField(blank=True, null=True)
    std_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    std_cnic = models.CharField(max_length=50, blank=True, null=True)
    father_cnic = models.CharField(max_length=50, blank=True, null=True)
    std_no = models.CharField(max_length=50, blank=True, null=True)
    father_no = models.CharField(max_length=50, blank=True, null=True)
    qualification = models.CharField(max_length=50)
    dob = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_degree_issued = models.BooleanField(default=False)

    def __str__(self):
        return self.student.username


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    clas = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=10)
    lectures = models.PositiveSmallIntegerField()
    attended = models.PositiveSmallIntegerField()
    leaves = models.PositiveSmallIntegerField()
    absents = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.student.student.username

class Exam(models.Model):
    clas = models.CharField(max_length=50, blank=True, null=True)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=50, unique=True)
    exam_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    date_time = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.exam_name

class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    clas = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    total_marks = models.PositiveSmallIntegerField()
    obtained_marks = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)



class Schedule(models.Model):
    clas = models.CharField(max_length=50, blank=True, null=True)
    start_year = models.PositiveSmallIntegerField() 
    end_year = models.PositiveSmallIntegerField()  
    course = models.CharField(max_length=50, unique=True)
    schedule_name = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.subject