from django.conf.urls import url
from.import views
urlpatterns=[
url(r'^$',views.hello,name ='index'),      # hello is function in view folder and index is nick name
url(r'htview/',views.hview,name='home'),         # hview is function in view folder and hview is url to open
url(r't11/',views.t11, name='hmm'),
url(r'orderr/',views.order_demo,name="ord"),
url(r'furr/',views.fur,name="furrr"),
url(r'reg/',views.register,name="regg"),
url(r'indexx/',views.temp,name="tempp"),
url(r'inh/',views.inh,name="inh"),
url(r'log/',views.Login,name="ll"),
#url(r'th',views.thanks,name='tgg'),
#url(r'emp/',views.employee,name='emp'),

    ]
