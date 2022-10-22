from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CreateUserForm

    list_display = ('get_html_photo', 'username', 'email', "date_joined",
                    "last_login", "is_active", 'is_staff')
    list_display_links = ('get_html_photo', 'username', 'email',)
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login')
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (
                ('get_html_photo', 'avatar'),
                ('username', 'email'), 'password',
            )
        }
         ),
        ("Особиста інформація", {
            "fields": (
                ("first_name", "last_name"),
            )
        }
         ),
        ("Дозволи", {
            "fields": (("is_active", "is_staff"), "is_superuser",
                       "groups", "user_permissions",
                       ),
        },
         ),
        ("Важливі дати", {
            "fields": (
                ("last_login", "date_joined"),
            )
        }
         ),

    )
    search_fields = ('username',)
    ordering = ('-date_joined',)
    readonly_fields = ('get_html_photo', 'date_joined', 'last_login')

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=35>")
        return 'No photo'

    get_html_photo.short_description = "Аватарка"



# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = CreateUserForm
#
#
# admin.site.register(User, CustomUserAdmin)
