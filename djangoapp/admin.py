from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'course')
    search_fields = ('age', 'course')
    list_filter = ('name', 'age', 'course')


admin.site.register(Student, StudentAdmin)
admin.site.register(Profile)
admin.site.register(Book)