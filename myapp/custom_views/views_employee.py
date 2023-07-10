from django.db.models import Q
from django.shortcuts import render, redirect
from myapp.models import Employee
from myapp.forms import EmployeeForm


def read(request):

    term = request.GET.get('term') if request.GET.get('term') is not None else ''
    # companies = Company.objects.filter(name__icontains=term)
    employee = Employee.objects.filter(
        Q(person__firstname__icontains=term) |
        Q(person__lastname__icontains=term) |
        Q(company__name__icontains=term)
    )

    return render(request, 'employees.html', {
         'title': 'Lista de empleados',
         'employees': employee,
         'search_title': 'Busca un Empleado...'
    })


def create(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees_view')

    return render(request, 'entity_form.html', {
        'title': 'Crear nuevo empleado',
        'form': form,
    })


def update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_view')

    return render(request, 'entity_form.html', {
        'title': f'Edicion de {employee.person}',
        'form': form
    })


def delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees_view')

    return render(request, 'entity_delete.html', {
        'entity': employee
    })