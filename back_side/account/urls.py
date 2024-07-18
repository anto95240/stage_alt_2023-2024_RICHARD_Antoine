from django.urls import path
from . import views

urlpatterns = [
    path('<str:role>-login/', views.role_login, name='role_login'),
    path('<str:role>-register/', views.role_register, name='role_register'),
    path('<str:role>/user/', views.get_user_details, name='get_user_details'),
    # path('<str:role>/user-update/', views.user_update, name='user_update')
]
