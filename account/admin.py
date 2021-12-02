from django import contrib
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, post
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'name')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(post)


admin.site.register(Account, AccountAdmin)