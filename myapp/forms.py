from django.forms import ModelForm
from .models import Person, Company, Employee


# Clase para formulario (hereda de django ModelForm)
class PersonForm(ModelForm):
    # Inner class (Meta)
    class Meta:
        # model hereda datos de Person
        model = Person
        # Fields debe traer todos los campos
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
