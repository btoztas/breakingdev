from django import forms
from calendarapp.models import StudentGroup, Event



class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentGroup
        fields = ['username', 'name', 'email', 'password', 'acro']


class RegisterEventForm(forms.ModelForm):

    time_start = forms.TimeField()
    time_end = forms.TimeField()
    date_start = forms.DateField()
    date_end = forms.DateField()

    class Meta:
        model = Event
        fields = ['time_start', 'time_end', 'date_start', 'date_end', 'title', 'description','image']


class EditEventForm(forms.ModelForm):

    time_start = forms.TimeField()
    time_end = forms.TimeField()
    date_start = forms.DateField()
    date_end = forms.DateField()
    event_id = forms.CharField()

    class Meta:
        model = Event
        fields = ['time_start', 'time_end', 'date_start', 'date_end', 'title', 'description', 'event_id']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = StudentGroup
        fields = ['name', 'email', 'description', 'image']
