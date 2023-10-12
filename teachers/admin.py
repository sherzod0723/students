from django.contrib import admin
from .models import Teachers, Students


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass