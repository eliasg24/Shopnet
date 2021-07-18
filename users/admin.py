# Django
from django.contrib import admin

# Models
from users.models import Profile

@admin.register(Profile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')
    search_fields = ('name', 'email')