from django import forms
class registerForm(forms.Form):
    rgid = forms.CharField(label="Enter Your Registration id", max_length=200)
    batch_code = forms.CharField(label="Enter Your Batch_code", max_length=200)
    name = forms.CharField(label="Enter Your Name", max_length=200)
    father_name = forms.CharField(label="Enter Your Father's Name", max_length=200)
    college = forms.CharField(label="Enter your college", max_length=200)
    contact = forms.CharField(label="Enter Your contact no.", max_length=200)
    email = forms.CharField(label="Enter Your email", max_length=200)
    CHOICES = [('IT_6months', 'IT_6months'), ('regular', 'regular')]
    time_period = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    #trainer_name = forms.CharField(label="Enter Your contact no.", max_length=200)
class signinForm(forms.Form):
    rgid1 = forms.CharField(label="Enter Your Registration id", max_length=200)


class TrainerSignInForm(forms.Form):
    empID = forms.CharField(label="Employee id", max_length=200)
    password = forms.CharField(label ="Password",max_length=200, widget=forms.PasswordInput)