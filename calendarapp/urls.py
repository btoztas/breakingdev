from django.conf.urls import url

from .views import HomePageView, LoginPageView, RegisterPageView, ForgotPasswordPageView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^index.html$', HomePageView.as_view(), name='home'),
    url(r'^login.html$', LoginPageView.as_view(), name='login'),
    url(r'^register.html$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot-password.html$', ForgotPasswordPageView.as_view(), name='resetPassword'),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="calendarapp/fullcalendar.html"), name='fullcalendar'),
    url(r'^fullcalendar2/', TemplateView.as_view(template_name="calendarapp/fullcalendar2.html"), name='fullcalendar'),

]
