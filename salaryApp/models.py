from django.db import models

class employeeModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    deparment=models.CharField(max_length=100, null=True)
    contact=models.CharField(max_length=20, null=True)
    joiningDate=models.DateField(auto_now_add=True, null=True)
    sex=models.CharField(max_length=10, null=True)
    bloodGroup=models.CharField(max_length=10, null=True)
    basicSalary=models.IntegerField()

class designationModel(models.Model):
    designation=models.CharField(max_length=100, null=True)
