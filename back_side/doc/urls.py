from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.get_user_documents, name='get_user_documents'),
]
