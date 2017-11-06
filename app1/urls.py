from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'gen', views.GenerateRandomUserFormView.as_view(), name='app1-gen-form'),
	url(r'', views.GenerateRandomUserView.as_view(), name='app1-gen'),
]