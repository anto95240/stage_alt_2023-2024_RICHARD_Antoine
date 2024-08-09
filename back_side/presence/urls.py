from django.urls import path
from . import views

urlpatterns = [
    path('presences/', views.get_presences, name='get_presences'),
]
