from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

# class Date(models.Model):
#     id = models.AutoField(primary_key=True)
#     date = models.DateField(unique=True, default=timezone.now)

#     def __str__(self):
#         return f'[{self.pk}]{str(self.date)}'

class Date(models.Model) :
    date = models.DateField(default=timezone.now)
    tempstr = timezone.now()
    strdate = models.CharField(max_length=30, default=tempstr.strftime("%Y-%m-%d"))
    
    def __str__(self) :
        return f'[{self.pk}]{str(self.date)}'

class Todo(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    mydate = models.DateField(default=timezone.now)
    tempstr = timezone.now()
    str_date = models.CharField(max_length=30, default=tempstr.strftime("%Y-%m-%d"))
    
    def __str__(self) :
        return f'[{self.pk}]{self.title}'