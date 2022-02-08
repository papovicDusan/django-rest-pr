from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
        
    title = models.CharField(max_length=50)    
    ONE = 'ON'
    TWO = 'TW'
    THREE = 'TH'
    PRIORITY_CHOICES = [
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
    ]
    priorty = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=ONE,
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="todo_list")
    
    def __str__(self):
        return self.title