from django.db import models

class Project(models.Model):
    Course = models.CharField(max_length=100)
    ProjectName = models.CharField(max_length=20)
    Grade = models.IntegerField()
    def __str__(self):
        return self.Course

class Exam(models.Model):
    Course = models.CharField(max_length=100)
    Date = models.DateField()
    Grade = models.IntegerField()
    def __str__(self):
        return self.Course
