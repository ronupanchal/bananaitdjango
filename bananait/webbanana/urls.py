from django.urls import path
from webbanana import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ourteam/', views.ourteam, name='ourteam'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('translation/', views.translate, name='translate'),
]