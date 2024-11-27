from django.contrib import admin

# Register your models here.
from .models import UserProfile, Avatar, BehaviorLog

admin.site.register(UserProfile)
admin.site.register(Avatar)
admin.site.register(BehaviorLog)

from .models import Avatar

