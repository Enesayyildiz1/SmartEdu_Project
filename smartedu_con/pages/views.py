import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses. models import Course
from pages.forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course']=Course.objects.filter(available=True).count()
        return context

#def index(request):
 #    return render(request, 'index.html')
# def about(request):
  #   return render(request, 'about.html')
class AboutView(TemplateView):
    template_name='about.html'

class ContactView(SuccessMessageMixin,FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('contact')
    success_message="We received your message successfully."

    def form_valid(self, form):
        form.save()
        logging.warning(form)
        return super().form_valid(form)

# Create your views here.
