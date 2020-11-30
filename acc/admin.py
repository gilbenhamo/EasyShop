from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import BusinessOwner,Customer

baseUser = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = baseUser

admin.site.register(baseUser,UserAdmin)
# Register your models here.
