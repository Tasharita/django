from django.contrib import admin
from hospitalapp.models import Users
from hospitalapp.models import Products,Member

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Member)
