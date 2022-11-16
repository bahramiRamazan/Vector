from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



from .models import User




class CustomUserAdmin(UserAdmin):
    model= User
    list=["user","name","email",'mobil','language_prefered']
admin.site.register(User,CustomUserAdmin)


