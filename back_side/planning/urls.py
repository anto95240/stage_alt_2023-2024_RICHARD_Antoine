from django.urls import path
from . import views

urlpatterns = [
    path('cours/', views.get_courses, name='get_courses'),
    path('search-students/', views.search_students, name='search_students'),
]
