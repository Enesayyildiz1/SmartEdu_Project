from django.urls import path
from . import views


urlpatterns = [
    path('', views.courselist,name="courses"),
    path('<int:course_id>/', views.course_detail,name="course_detail"),
]