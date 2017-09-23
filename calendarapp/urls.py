from django.conf.urls import url
from .views import HomePageView, RegisterPageView, ForgotPasswordPageView, ProfilePageView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$',  HomePageView.as_view(), name='home'),
    url(r'^dashboard$', TemplateView.as_view(template_name="calendarapp/fullcalendar.html"), name='dashboard'),
    url(r'^login$', auth_views.login, {'template_name': 'calendarapp/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^register$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot-password$', ForgotPasswordPageView.as_view(), name='resetPassword'),
    url(r'^profile$', ProfilePageView.as_view(), name='profile'),
    url(r'^newEvent', TemplateView.as_view(template_name="calendarapp/createEvent.html"), name='newevent'),

]
