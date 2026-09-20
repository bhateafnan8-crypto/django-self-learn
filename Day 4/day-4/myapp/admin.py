from django.contrib import admin
from myapp.models import Student
from myapp.models import students
# Register your models here.

admin.site.register(Student)

@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ['name','is_pass','email','gr_num']
    list_filter = ['is_pass','name']
    search_fields = ['gr_num','name']
