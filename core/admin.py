from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext as _
from .models import User

class UserAdmin(BaseUserAdmin):

    ordering = ['id']
    list_display = ['email', 'phone_number', 'first_name', 'last_name']
    fieldsets = (
        (None, {"fields": ('email', 'password', 'phone_number')}),
        (_('Personal _Info'), {'fields': ('first_name', 'last_name')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
        )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'first_name', 'last_name', 'address', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)