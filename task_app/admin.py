from django.contrib import admin
from task_app.models import Category, Doctor
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


class DoctorAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'birth_date']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Doctor, DoctorAdmin)