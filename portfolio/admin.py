from django.contrib import admin

from .models import Project, Exam

admin.site.register(Project)
admin.site.register(Exam)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Grade')

class ExamAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Grade')
