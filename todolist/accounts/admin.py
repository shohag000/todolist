from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','is_admin','is_staff')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('username','email','password')}),
        ('Permissions',{'fields':('is_admin','is_staff')}),
    )
    search_fields = ('username','email')
    ordering = ('username','email')
    filter_horizontal = ()


admin.site.register(MyUser,UserAdmin)

admin.site.unregister(Group)