from faker import Faker
from .models import *
import random
from django.db.models import Sum

fake = Faker()

def seed_db(n = 20):
    try:
        for i in range(n):
            department_object = Department.objects.all()
            random_department_index = random.randint(0, len(department_object)-1)
            department = department_object[random_department_index]
            student_id = f'STU-{random.randint(0,1000)}'
            student_name = fake.name()
            student_age = random.randint(18,25)
            student_email = fake.email()
            student_address = fake.address()
            
            student_id_obj = StudentID.objects.create(
                student_id = student_id
            )
            
            Student.objects.create(
                department_name = department, 
                student_name = student_name,
                student_age = student_age,
                student_email = student_email,
                student_address = student_address,
                student_id = student_id_obj
            )
            
        print(f'Created fake data of {n} students')
        
    except Exception as e:
        print(e)
        
def generate_student_marks():
    try:
        students = Student.objects.all()
        for student in students:
            subject_object = Subject.objects.all()
            for subject in subject_object:
                SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(1,100)
                )
            
    except Exception as e:
        print(e)
            
def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks')
    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i+=1
        
        