from django.urls import path
from . import views
from pages.views import AboutView,IndexView,ContactView


urlpatterns = [
    #path('index/', views.index,name="index"),
    path('index/', IndexView.as_view(),name="index"),
    #path('about/', views.about,name="about"),
    path('about/', AboutView.as_view(),name="about"),
    path('contact/', ContactView.as_view(),name="contact"),

  
]
#yönlendirme