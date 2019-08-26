from django.contrib import admin
from myapp.models import web1
from myapp.models import News
from myapp.models import tb_registration
from myapp.models import employee
# Register your models here.
admin.site.register(web1)
admin.site.register(News)
admin.site.register(tb_registration)
admin.site.register(employee)

