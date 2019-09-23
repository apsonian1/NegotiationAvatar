from django.contrib import admin
from .models import Purpose
from .models import UserProfile


admin.site.register(Purpose)
admin.site.register(UserProfile)