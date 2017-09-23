from django.conf.urls import url

from .views import HomePageView, LoginPageView, RegisterPageView, ForgotPasswordPageView, ProfilePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^index.html$', HomePageView.as_view(), name='home'),
    url(r'^login.html$', LoginPageView.as_view(), name='login'),
    url(r'^register.html$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot-password.html$', ForgotPasswordPageView.as_view(), name='resetPassword'),
    url(r'^profile.html$', ProfilePageView.as_view(), name='profile'),
]
