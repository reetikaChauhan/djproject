from django.contrib import admin
from myApp.models import signIn
from myApp.models import TrainerSignIn

# Register your models here.
admin.site.register(signIn)
admin.site.register(TrainerSignIn)