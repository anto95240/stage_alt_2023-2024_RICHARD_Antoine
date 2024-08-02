from django.contrib import admin

from .models import Course
from user.models import User

class CourseAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Teacher":
            kwargs["queryset"] = User.objects.filter(Role='teacher')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Course, CourseAdmin)