from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^output/', views.get_digits, name='get_digits'),
	url(r'^$', views.get_digits, name='get_digits'),
]