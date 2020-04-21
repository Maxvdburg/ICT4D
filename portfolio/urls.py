from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'portfolio/detail.html', {'project': project})
