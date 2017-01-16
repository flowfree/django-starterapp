from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^change_password/$', views.change_password),
]