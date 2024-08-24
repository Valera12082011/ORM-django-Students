from django.db import models

from Student.models import Student
from Subject.models import Subject

class Grade( models.Model ):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    grade = models.IntegerField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.grade}'
