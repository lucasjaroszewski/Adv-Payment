from django.contrib import admin
from apps.users.models import User, Payment

admin.site.register(User)
admin.site.register(Payment)
