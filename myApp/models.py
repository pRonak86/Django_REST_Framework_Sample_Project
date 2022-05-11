from django.db import models

# Create your models here.
class Student(models.Model):
    StudentName=models.CharField(max_length=30)
    StudentLastName=models.CharField(max_length=30)
    StudentContact=models.BigIntegerField()

    def __str__(self):
        return self.StudentName
