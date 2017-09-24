from django.conf.urls import url
from .views import HomePageView, RegisterPageView, ForgotPasswordPageView, ProfilePageView, HomePage2View, \
    CreateEventView, EventView, DashboardView, ListEventsView, EditEventView, DeleteEventView, EditProfileView

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [

    # HOME
    url(r'^$',  HomePageView.as_view(), name='home'),
    url(r'^profile/(?P<profile_id>\d+)/$', ProfilePageView.as_view(), name='profile'),
    url(r'^event/(?P<event_id>\d+)/$',  EventView.as_view(), name='event'),


    # DASHBOARD
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/new-event/$', CreateEventView.as_view(), name='create_event'),
    url(r'^dashboard/list-events/$', ListEventsView.as_view(), name='list_events'),
    url(r'^dashboard/edit-event/$', EditEventView.as_view(), name='edit_event'),
    url(r'^dashboard/delete-event/$', DeleteEventView.as_view(), name='delete_event'),

    url(r'^dashboard/edit-profile/$', EditProfileView.as_view(), name='edit_profile'),


    # LOGIN/LOGOUT/USER
    url(r'^login/$', auth_views.login, {'template_name': 'calendarapp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/calendarapp/'}, name='logout'),
    url(r'^register/$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot-password/$', ForgotPasswordPageView.as_view(), name='resetPassword'),
]
