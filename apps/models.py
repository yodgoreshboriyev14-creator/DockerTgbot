from django.db import models

# Create your models here.

from django.db.models import Model, BigIntegerField , CharField


class TelegramUser(Model):
    telegram_id = BigIntegerField(unique=True)
    full_name = CharField(max_length=255)
    username = CharField(max_length=255, null=True, blank=True)
    phone_number = CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
