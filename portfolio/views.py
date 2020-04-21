from django.template import loader
from django.shortcuts import render


from .models import Project, Exam

def index(request):
    latest_project_list = Project.objects.order_by('Course')[:5]
    latest_exam_list = Exam.objects.order_by('Course')[:5]
    context = {'latest_project_list': latest_project_list, 'latest_exam_list': latest_exam_list}
    return render(request, 'portfolio/index.html', context)
