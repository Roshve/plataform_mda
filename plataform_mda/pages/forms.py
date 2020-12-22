from django import forms

class form_new_user(forms.Form):

    #Form Leader
    leader_email = forms.EmailField(input='leader_email', max_length=320)
    leader_name = forms.CharField(input='leader_name', max_length=100)
    leader_lastname = forms.CharField(input='leader_lastname', max_length=100)
    cost_center = forms.IntegerField(input='cost_center', min_value=3, max_value=3)
    product =  forms.IntegerField(input='product', min_value=0, max_value=6)

    #Form New Employee
    employee_name = forms.CharField(input='employee_name', max_length=100)
    employee_lastname = forms.CharField(input='employee_lastname', max_length=100)
    management_consulting = forms.CharField(input='management_consulting', max_length=100)
    employee_dni = forms.IntegerField(input='employee_dni', min_value=0 , max_value=12)
    profile_equal = forms.CharField(input='profile_equal', max_length=100)
    employee_replace = forms.CharField(input='employee_replace', max_length=100)

    #Form Device-Work

    