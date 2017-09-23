from django import forms
from calendarapp.models import StudentGroup
from schedule.models import Event


class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentGroup
        fields = ['username', 'name', 'email', 'password']


class RegisterEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['start', 'end', 'title', 'description']
