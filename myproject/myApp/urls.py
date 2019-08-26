from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.hello,name="id"),
    url(r'log/',views.Login,name="ll"),
    url(r'sign/',views.signin,name="si"),
    url(r'tra',views.TrainerSignIn,name="ts"),
]