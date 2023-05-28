from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

##########################################################################


class UsersAdmin(UserAdmin):
    list_display = (
        "username",
        "is_active",
        "is_staff",
        "id",
        "dni",
        "phone_number",
        "country"
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'dni', 'email',
         'country', 'city', 'address', 'number_address', 'phone_number', 'image_user')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    list_per_page = 25


##########################################################################


admin.site.register(Users, UsersAdmin)
