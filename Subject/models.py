from django.db import models

class Subject( models.Model ):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.code}"