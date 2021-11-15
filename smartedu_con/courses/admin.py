from django.contrib import admin
from . models import Category, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available')
    list_filter=('available',)
    search_fields=('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
# Register your models here.
