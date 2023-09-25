from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "nome", "sobrenome", "ocupacao", "cidade", "estado", "celular")
    list_filter = ("email", "is_staff", "is_active", "nome", "sobrenome", "ocupacao", "cidade", "estado", "celular")
    fieldsets = (
        (None, {"fields": ("email", "password", "nome", "sobrenome", "ocupacao", "cidade", "estado", "celular")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "nome", "sobrenome", "ocupacao", "cidade", "estado", "celular", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)