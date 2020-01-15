from django.contrib import admin
from .models import UserProfile # importing models to be shown in admin panel
# Register your models here.
admin.site.register(UserProfile) # registering UserProfile model to show in admin