from django import forms
from calendarapp.models import StudentGroup


class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentGroup
        fields = ['username', 'name', 'email', 'password']
