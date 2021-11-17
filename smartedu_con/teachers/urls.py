from django.urls import path
from teachers.models import Teacher
from . import views
from teachers.views import TeacherListView,TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(),name="teachers"),
    path('<slug:slug>',TeacherDetailView.as_view(),name="teacher_detail")
]