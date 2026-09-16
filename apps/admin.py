from django.contrib import admin

# Register your models here.

from django.contrib import admin

from apps.models import TelegramUser

admin.site.register(TelegramUser)