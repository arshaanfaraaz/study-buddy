from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Sum


# Create your views here.
def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q (student_name__icontains = search) |
            Q (student_age__icontains = search) |
            Q(department_name__department_name__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_id__student_id__icontains = search)
        )
    paginator = Paginator(queryset, 12)  # Show 12 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'queryset': page_obj}
    return render(request, 'student_list.html', context)


def get_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(marks = Sum("marks"))
    context = {'queryset': queryset, 'total_marks': total_marks}
    return render(
        request, 
        'student.html',
        context
    )