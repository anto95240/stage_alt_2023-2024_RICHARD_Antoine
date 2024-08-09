from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_student_notes, name='get_student_notes'),
]
