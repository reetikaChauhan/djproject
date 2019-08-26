from django import forms
class RegistrationForm1(forms.Form):
    BIRTH_YEAR_CHOICES = ['1996', '1997', '1982']
    name = forms.CharField(label="Enter Your Name", max_length=200)
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    contact = forms.CharField(label="Enter Your Contact", max_length=200)
    address = forms.CharField(label="Enter Your Address", max_length=200)
    password = forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)
    birth_year = forms.DateField(widget=forms.SelectDateWidget (years=BIRTH_YEAR_CHOICES))
    CHOICES=[('Male','Male'),('Female','Female')]
    Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
class LoginForm1(forms.Form):
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password = forms.CharField(label="Enter Your Password", max_length=200, widget=forms.PasswordInput)

class employeeForm(forms.Form):
    Job_title = forms.CharField(label="Enter job title", max_length=200)
    #ename = forms.CharField(label="Enter name", max_length=200)
    Specialization = forms.CharField(label="Enter specialization", max_length=200)
    experience = forms.CharField(label="Enter experience", max_length=200)

