from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Date(models.Model) :
    date = models.DateField(default=timezone.now)
    tempstr = timezone.now()
    strdate = models.CharField(max_length=30, default=tempstr.strftime("%Y-%m-%d"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'[{self.pk}]{str(self.date)}'

class Todo(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    mydate = models.DateField(default=timezone.now)
    tempstr = timezone.now()
    str_date = models.CharField(max_length=30, default=tempstr.strftime("%Y-%m-%d"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'[{self.pk}]{self.title}'