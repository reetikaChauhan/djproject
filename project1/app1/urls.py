from django.conf.urls import url
from .import views
urlpatterns=[
url(r'^$',views.hey,name='index'),
url(r'happy',views.hi,name='index1'),
url(r'ide',views.idd,name='index2'),
url(r'reg',views.register,name='index2')
#url(r'log',views.LoginForm1,name='lg'),
]