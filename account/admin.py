from django.contrib import admin
from .models import User, Customer, Business, superMassage, Categories
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.admin.models import LogEntry

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(superMassage, SimpleHistoryAdmin)
admin.site.register(Categories)
admin.site.register(LogEntry)
