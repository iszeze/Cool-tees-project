from django.contrib import admin

# Register your models here.
from .models import User
@admin.register(User)
class UserModel(admin.ModelAdmin):
    fields = ['user_name', 'email','token', 'token_expires_at']
    list_filter = []
    list_display = fields
    search_fields = ['user_name', 'email']
