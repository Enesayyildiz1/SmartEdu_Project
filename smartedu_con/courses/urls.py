from django.urls import path
from . import views


urlpatterns = [
    path('', views.courselist,name="courses"),
    path('<int:course_id>/', views.course_detail,name="course_detail"),
    path('categories/<slug:category_slug>', views.courses_by_category,name="courses_by_category"),
    path('tags/<slug:tag_slug>', views.courses_by_tags,name="courses_by_tags")
]