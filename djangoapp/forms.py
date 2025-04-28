from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#django form
class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Enter your Email')
    enquiry = forms.CharField(label='your enquiries', widget=forms.Textarea)

#Model Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'course', 'doc', 'img']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']