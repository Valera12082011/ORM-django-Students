from django.db import models

class Student( models.Model ):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    data_of_birth_day = models.DateField()
    group_number = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.first_name}'