from django.urls import path
from . import views


urlpatterns = [
    path('', views.courselist,name="courses"),
    path('<int:course_id>/', views.course_detail,name="course_detail"),
    path('categories/<slug:category_slug>', views.courselist,name="courses_by_category"),
    path('tags/<slug:tag_slug>', views.courselist,name="courses_by_tags"),
    path('search/', views.search,name="courses_by_key")
]