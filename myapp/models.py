from django.db import models
from datetime import date

# Create your models here.
## Schema
class ToDoItems(models.Model):
    title=models.CharField(max_length=200) 
    deadline=models.DateField(default=date.today)
    completed=models.BooleanField(default=False) 
