from django.contrib import admin
from .models import User, Customer, Business , superMassage ,Categories
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(superMassage,SimpleHistoryAdmin)
admin.site.register(Categories)