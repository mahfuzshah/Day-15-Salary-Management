from django.shortcuts import render
from salaryApp.models import employeeModel, salaryModel

def addemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        deparment = request.POST.get('deparment')
        contact = request.POST.get('contact')
        sex = request.POST.get('sex')
        bloodGroup = request.POST.get('bloodGroup')
        basicSalary = int(request.POST.get('basicSalary'))
        
        employee = employeeModel(
            name=name,
            designation=designation,
            deparment=deparment,
            contact=contact,
            sex=sex,
            bloodGroup=bloodGroup,
            basicSalary=basicSalary
        )
        employee.save()
    return render(request, 'salaryApp/addemployee.html')

def employeeList(request):
    employees = employeeModel.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'salaryApp/employeeList.html', context)

def editemployee(request, employee_id):
    employee = employeeModel.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.designation = request.POST.get('designation')
        employee.deparment = request.POST.get('deparment')
        employee.contact = request.POST.get('contact')
        employee.sex = request.POST.get('sex')
        employee.bloodGroup = request.POST.get('bloodGroup')
        employee.basicSalary = int(request.POST.get('basicSalary'))
        employee.save()
    context = {
        'employee': employee,
    }
    return render(request, 'salaryApp/editemployee.html', context)


def employeeDetail(request, employee_id):
    employee = employeeModel.objects.get(id=employee_id)
    salaries = salaryModel.objects.filter(employee=employee)
    context = {
        "employee": employee,
        "salaries": salaries,
    }
    return render(request, "salaryApp/employeeDetail.html", context)

def deleteemployee(request, employee_id):
    employee = employeeModel.objects.get(id=employee_id)
    employee.delete()
    employees = employeeModel.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'salaryApp/employeeList.html', context)


def addSalary(request):

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        month = request.POST.get("month")
        year = request.POST.get("year")
        totalDays = int(request.POST.get("totalDays"))
        presentDays = int(request.POST.get("presentDays"))
        absentDays = int(request.POST.get("absentDays"))
        leaveDays = int(request.POST.get("leaveDays"))
        grossSalary = int(request.POST.get("grossSalary"))
        pfAmount = int(request.POST.get("pfAmount"))
        taxAmount = int(request.POST.get("taxAmount"))
        netSalary = grossSalary - pfAmount - taxAmount

        employee = employeeModel.objects.get(id=employee_id)
        salary = salaryModel(
            employee=employee,
            month=month,
            year=year,
            totalDays=totalDays,
            presentDays=presentDays,
            absentDays=absentDays,
            leaveDays=leaveDays,
            grossSalary=grossSalary,
            pfAmount=pfAmount,
            taxAmount=taxAmount,
            netSalary=netSalary,
        )
        salary.save()

    context = {
        "employees": employees,
    }
    return render(request, "salaryApp/addSalary.html", context)


def salaryHome(request):
    employees = employeeModel.objects.all()
    salaries = salaryModel.objects.all()
    context = {
        'employees': employees,
        'salaries': salaries,
    }
    return render(request, 'salaryApp/salaryHome.html', context)


def salaryReport(request):
    salaries = salaryModel.objects.all()
    context = {
        'salaries': salaries,
    }
    return render(request, 'salaryApp/salaryReport.html', context) 
