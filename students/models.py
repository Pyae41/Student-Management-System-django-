from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    study_field = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.name}'
    