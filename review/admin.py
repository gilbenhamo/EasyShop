from django.contrib import admin
from .models import comments
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(comments,SimpleHistoryAdmin)


