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

    def __str__(self):
        return self.name
class salaryModel(models.Model):
    employee=models.ForeignKey(employeeModel, on_delete=models.CASCADE)
    month=models.CharField(max_length=20, null=True)
    year=models.CharField(max_length=10, null=True)
    totalDays=models.IntegerField(null=True)
    presentDays=models.IntegerField(null=True)
    absentDays=models.IntegerField(null=True)
    leaveDays=models.IntegerField(null=True)
    grossSalary=models.IntegerField(null=True)
    pfAmount=models.IntegerField(null=True)
    taxAmount=models.IntegerField(null=True)
    netSalary=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.employee.name} - {self.month} {self.year}"
