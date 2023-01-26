from django.contrib import admin

# Register your models here.

from vfapp.models import MyUser

admin.site.register(MyUser)