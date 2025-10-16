from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add your custom fields to the admin form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Add custom fields to the user creation form in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Show extra info in the user list
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')


# Register the custom user model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
