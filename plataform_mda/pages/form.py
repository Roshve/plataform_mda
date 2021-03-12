from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class FormNewUser(forms.Form):

    #Form Leader
    leader_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Federico' }), max_length=100)
    leader_lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'De Bernardi' }), max_length=100)
    leader_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control ','placeholder': 'fdebernardi@lanacion.com.ar' }), max_length=320) 
    cost_center = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': '708' }), max_length=3)
    product =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': '1313AZ' }), max_length=6)

    #Form NewUser
    yes_no = [('Si', 'Si'), ('No', 'No')]
    intern_extern = [('Interno', 'Interno'), ('Externo','Externo')]
    newuser_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Alvin' }), max_length=100)
    newuser_lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Yakitori' }), max_length=100)
    entry_method = forms.ChoiceField(widget=forms.RadioSelect, choices=(intern_extern))
    external_company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Macsoul' }), max_length=100)
    replace_someone = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    who_is = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Yeferson Guitierritos' }), max_length=100)
    similar_profile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Christian Leguizamon' }), max_length=100)
    date_of_admission = forms.DateField(widget=DateInput(attrs={'class': 'form-control ','min':'2021-03-01'}))
    
    #Form Devices
    devices_options = [('PC', 'PC'), ('MAC', 'MAC'), ('Notebook', 'Notebook'), ('No', 'No')]
    cellphone_options = [('Cesion', 'Cesion'), ('Nueva Linea', 'Nueva Linea'), ('No', 'No')]
    cellphone_line_options = [('Movistar', 'Movistar'), ('Claro', 'Claro')]
    
    devices = forms.ChoiceField(widget=forms.RadioSelect, choices=(devices_options))
    re_use_devices = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    
    cellphone = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    re_use_cellphone = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    service_phone = forms.ChoiceField(widget=forms.RadioSelect, choices=(cellphone_options))
    cellphone_line = forms.ChoiceField(widget=forms.RadioSelect, choices=(cellphone_line_options))
    re_use_cellphone_line = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    phone = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))

    #Form ConfigUser
    prepare_device_options = [('Basico', 'Basico'), ('Redacción', 'Redacción'), ('Desarrollo', 'Desarrollo')]
    prepare_device = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control '}), choices=(prepare_device_options))
    apps_device = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control ', 'rows':'10'}))
    licens_365 = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))
    double_boot = forms.ChoiceField(widget=forms.RadioSelect, choices=(yes_no))