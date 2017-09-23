from django.conf.urls import url

from .views import HomePageView, RegisterPageView, ForgotPasswordPageView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^login$', auth_views.login, {'template_name': 'calendarapp/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^register$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot-password$', ForgotPasswordPageView.as_view(), name='resetPassword'),
    url(r'^forgot-password.html$', ForgotPasswordPageView.as_view(), name='resetPassword'),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="calendarapp/fullcalendar.html"), name='fullcalendar'),
    url(r'^fullcalendar2/', TemplateView.as_view(template_name="calendarapp/fullcalendar2.html"), name='fullcalendar'),
]
