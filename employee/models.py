from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=20)
    class Meta:
        db_table = 'employee'
