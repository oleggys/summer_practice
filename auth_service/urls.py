from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_view, name='login_page'),
    path('registration', views.registration_view, name='registration_page'),
    path('logout', views.logout_view, name='logout')
]
