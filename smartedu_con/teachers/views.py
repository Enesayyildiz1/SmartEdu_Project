from django.shortcuts import render
from teachers. models import Teacher
from courses. models import Course
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


teachers=Teacher.objects.all()


class TeacherListView(ListView):
    paginate_by = 2
    model=Teacher
    template_name='teachers.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model=Teacher
    template_name='teacher.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True,teacher=self.object)
        return context
        #course sayfasına öğretmen bilgisini çek
        #tekil teacher sayfasını düzenle
        #ilgili linkleri düzenle



    
# Create your views here.
