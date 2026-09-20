from django.contrib import admin
from stdapp.models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "email", "course")
    list_filter = ("course",)
    search_fields = ("name", "email", "course")

admin.site.register(Student,StudentAdmin)