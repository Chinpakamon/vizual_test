from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'registration_date', 'password')
    search_fields = ('username', 'email',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
