from django.contrib import admin

from .models import *
from user.models import User

class PresenceAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Student":
            kwargs["queryset"] = User.objects.filter(Role='student')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Presence, PresenceAdmin)