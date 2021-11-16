from django.contrib import admin
from . models import Category, Course,Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available','category')
    list_filter=('available',)
    search_fields=('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
# Register your models here.
