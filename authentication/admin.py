from django.contrib import admin

from authentication.models import customUser

# Register your models here.

from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    list_display=["username","user_type"]

admin.site.register(customUser,userModel)


