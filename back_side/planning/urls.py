from django.urls import path
from . import views

urlpatterns = [
    path('cours/', views.get_courses, name='get_courses'),
]
