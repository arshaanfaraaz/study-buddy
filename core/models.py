from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department_name
    
    
    class Meta():
        ordering = ['department_name']
        
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name='departmenttable')
    student_id = models.OneToOneField(StudentID, on_delete=models.CASCADE, related_name='studentid', null=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    student_email = models.EmailField(unique=True)
    student_address = models.TextField()
    
    def __str__(self) -> str:
        return self.student_name
    
    class Meta():
        ordering = ['student_name']
        
class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='studentprofile')


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.subject_name
    
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='studentmarks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    class Meta:
        unique_together = ['student', 'subject']
    
    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name='studentreportcard', on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_generation = models.DateField(auto_now=True)
    
    
    unique_together = ['student_rank', 'date_of_generation']